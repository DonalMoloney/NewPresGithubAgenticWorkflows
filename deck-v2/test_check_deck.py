import os
import tempfile
import unittest

from check_deck import check, split_slides

FRONT = "---\nmarp: true\n---\n\n"


def run(md, files=()):
    with tempfile.TemporaryDirectory() as d:
        for f in files:
            os.makedirs(os.path.dirname(os.path.join(d, f)) or d, exist_ok=True)
            open(os.path.join(d, f), "w").close()
        path = os.path.join(d, "deck.md")
        with open(path, "w") as fh:
            fh.write(FRONT + md)
        return check(path)


class SplitSlides(unittest.TestCase):
    def test_ignores_rule_inside_code_fence(self):
        md = FRONT + "# A\n\n```markdown\n---\nx\n---\n```\n\n---\n\n# B\n"
        self.assertEqual(len(split_slides(md)), 2)


class Check(unittest.TestCase):
    def test_clean_deck_passes(self):
        errors, _ = run("# A\n\n<!--\nnote\n-->\n")
        self.assertEqual(errors, [])

    def test_directive_is_not_a_note(self):
        errors, _ = run("<!-- header: Why -->\n\n# A\n")
        self.assertTrue(any("no speaker note" in e for e in errors))

    def test_note_starting_with_todo_is_a_note(self):
        errors, _ = run("# A\n\n<!--\nTODO: tell the story.\n-->\n")
        self.assertEqual(errors, [])

    def test_small_body_font_fails(self):
        errors, _ = run("<style scoped>p { font-size: 18px; }</style>\n\n# A\n\n<!--\nn\n-->\n")
        self.assertTrue(any("18px" in e for e in errors))

    def test_code_may_be_18px(self):
        errors, _ = run("<style scoped>pre { font-size: 18px; }</style>\n\n# A\n\n<!--\nn\n-->\n")
        self.assertEqual(errors, [])

    def test_missing_image_fails(self):
        errors, _ = run("# A\n\n![alt w:100](img/x.svg)\n\n<!--\nn\n-->\n")
        self.assertTrue(any("img/x.svg" in e for e in errors))

    def test_present_image_passes(self):
        errors, _ = run("# A\n\n![alt w:100](img/x.svg)\n\n<!--\nn\n-->\n", files=["img/x.svg"])
        self.assertEqual(errors, [])

    def test_visible_todo_is_a_warning(self):
        errors, warnings = run('# A\n\n<span class="todo">TODO</span>\n\n<!--\nn\n-->\n')
        self.assertEqual(errors, [])
        self.assertTrue(any("TODO" in w for w in warnings))


if __name__ == "__main__":
    unittest.main()
