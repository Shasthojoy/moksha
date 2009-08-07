from paver.easy import *
from paver.setuputils import (setup, find_package_data, find_packages,
                              install_distutils_tasks)
from moksha.lib.paver_tasks import *

install_distutils_tasks()

options(
    setup=Bunch(
        name="moksha.docs",
        version="1.0",
        release="1",
        url="http://moksha.fedorahosted.org",
        description="Moksha Docs App",
        long_description="TODO.",
        license='AGPLv3',
        rpm_name='moksha-apps-docs',
        author="Luke Macken",
        author_email="lmacken@redhat.com",
        packages=find_packages(),
        package_data=find_package_data(),
        install_requires=["Moksha"],
        namespace_packages=['moksha'],
        entry_points={
            'moksha.application': (
                'docs = moksha.apps.docs.docs:docs',
            ),
        }
    ),
)