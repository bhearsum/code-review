from functools import cached_property

from libmozdata.phabricator import UnitResult, UnitResultState

from code_review_bot import BaseIssue, IssueType, Level
from code_review_bot.tasks.base import AnalysisTask


class BuildIssue(BaseIssue):
    type_ = IssueType.BuildTest

    @cached_property
    def hash(self):
        return "hash representation"

    def is_publishable(self):
        # should this always be true?
        return True

    def validates(self):
        # TODO: when should this be false? ever? what does this even mean?
        return True

    def as_text(self):
        return "text repsentation"

    def as_markdown(self):
        return "markdown representation"

    def as_markdown_for_phab(self):
        return "markdown for phab representation"

    def as_error(self):
        return "error representation"

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
        issues = []

        if self.state == "failed":
            issues.append(
                BuildIssue(
                    analyzer=self,
                    revision=revision,
                    level=Level.Error,
                    message="Build failed!",
                )
            )

        return issues
