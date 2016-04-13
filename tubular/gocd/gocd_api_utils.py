"""
Utility functions using the GoCD API via the requests module.
"""
import os
import requests
from tubular.scripts.github.github_api_utils import GitHubApiUtils


GOCD_API_URL = "http://localhost:8153"
TRIGGER_POST = "/go/api/pipelines/{}/schedule"
GITHUB_BASE_URL = "https://github.com/{}"


class GoCDApiUtils(object):
    """
    Class to query/set GoCD info.
    """
    def __init__(self):
        """
        Authenticates a GoCD user.
        """
        self.gocd_username = os.environ.get('GOCD_USERNAME', '')
        self.gocd_password = os.environ.get('GOCD_PASSWORD', '')

    def trigger_pipeline(self, pipeline_name, repo, pr_id):
        """
        Given a pipeline_name and GitHub repo/PR, trigger a pipeline run for a build/deploy.
        """
        if not self.gocd_username or not self.gocd_password:
            # No auth creds.
            return False

        if not pipeline_name or not repo or not pr_id:
            # Bad params.
            return False

        # Using the repository and PR number, find the commit hash to use.
        g = GitHubApiUtils(repo)
        commit_hash = g.get_head_commit_from_pr(pr_id)

        trigger_payload = {
            "variables[GO_EXTERNAL_TRIGGER_PR_ID]": pr_id,
            "variables[GO_EXTERNAL_TRIGGER_REPO_URL]": GITHUB_BASE_URL.format(repo),
            "variables[GO_EXTERNAL_TRIGGER_COMMIT_HASH]": commit_hash,
        }
        post_url = GOCD_API_URL + TRIGGER_POST.format(pipeline_name)
        r = requests.post(
            post_url,
            auth=(self.gocd_username, self.gocd_password),
            params=trigger_payload,
        )
        success = r.status_code in (202,)
        if not success:
            print "Error {}: {}: Pipeline {} failed to trigger.\n{}".format(r.status_code, r.content, pipeline_name, post_url)
        return success