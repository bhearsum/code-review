from functools import cached_property

from libmozdata.phabricator import UnitResult, UnitResultState

from code_review_bot import BaseIssue
from code_review_bot.tasks.base import AnalysisTask


class BuildIssue(BaseIssue):
    @cached_property
    def hash(self):
        # TODO
        return "foo"

    def validates(self):
        return False

    def as_text(self):
        return "TODO"

    def as_markdown(self):
        return "TODO"

    def as_error(self):
        return "TODO"

    def is_build_error(self):
        return True

    def as_phabricator_issue(self):
        return UnitResult(
            namespace="code-review",
            name="general",
            result=UnitResultState.Fail,
            details=f"Code review bot found a **build error**: \n{self.message}",
            format="remarkup",
        )


class BuildTask(AnalysisTask):
    def parse_issues(self, artifacts, revision):
        pass
