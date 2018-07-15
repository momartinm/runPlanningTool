import os
from subprocess import check_call, check_output, CalledProcessError

from paths import makedirs

def is_mercurial_repo(url):
    try:
        check_call(["hg", "id", url])
        return True
    except CalledProcessError:
        return False

def is_git_repo(url):
    try:
        check_call(["git", "ls-remote", url])
        return True
    except CalledProcessError:
        return False

def detect_repo_type(url):
    if is_mercurial_repo(url):
        return "hg"
    elif is_git_repo(url):
        return "git"
    else:
        assert False, "Repository type of '%s' cannot be detected or is not supported" % url

def clone(repo_type, url, repo_dir):
    makedirs(os.path.dirname(repo_dir))
    if repo_type == "hg":
        check_call(["hg", "clone", url, repo_dir])
    else:
        assert repo_type == "git"
        check_call(["git", "clone", url, repo_dir])

def pull(repo_type, repo_dir):
    if repo_type == "hg":
        check_call(["hg", "--cwd", repo_dir, "pull"])
    else:
        assert repo_type == "git"
        check_call(["git", "-C", repo_dir, "fetch", "--all"])

def get_up_to_date_repo(repo_type, url, repo_dir):
    if os.path.exists(repo_dir):
        pull(repo_type, repo_dir)
    else:
        clone(repo_type, url, repo_dir)

def get_tag_revision(repo_type, repo_dir, tag):
    try:
        if repo_type == "hg":
            output = check_output(["hg", "--cwd", repo_dir, "id", "-i", "-r", tag])
        else:
            assert repo_type == "git"
            output = check_output(["git", "-C", repo_dir, "rev-parse", "origin/" + tag])
    except CalledProcessError:
        return None
    return output.decode().strip()[:8]


def update(repo_type, repo_dir, tag):
    if repo_type == "hg":
        check_call(["hg", "--cwd", repo_dir, "update", tag, "-C"])
    else:
        assert repo_type == "git"
        check_call(["git", "-C", repo_dir, "reset", "--hard"])
        check_call(["git", "-C", repo_dir, "clean", "-d", "-x", "-f"])
        check_call(["git", "-C", repo_dir, "checkout", "origin/%s" % tag])
#        check_call(["git", "-C", repo_dir, "merge"])
