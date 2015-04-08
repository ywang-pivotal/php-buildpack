from nose.tools import eq_
# from nose.tools import raises
from build_pack_utils import cloudfoundry


class TestCloudFoundrInstaller(object):

    def test_missing_dependency_from_manifest_raises_error(self):
        try:
            instance = cloudfoundry.CloudFoundryInstaller({
                'CACHE_DIR': '/cache/dir',
                'BUILD_DIR': 'tests/data/composer',
                'BP_DIR': '',
                'TESTING_DOWNLOAD_URL': ''
            })
            instance.install_binary('TESTING')
        except RuntimeError as e:
            eq_("Could not get translated url, exited with: DEPENDENCY_MISSING_IN_MANIFEST:", e.message)
