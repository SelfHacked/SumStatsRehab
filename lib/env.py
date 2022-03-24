# standard library
import os



class WrongRuntimeEnvironmentVariable(Exception):
    pass


GWASSS_BUILD_NUMBER_ENV = 'build_num'


def get_build() -> str:
    build = os.getenv(GWASSS_BUILD_NUMBER_ENV)
    if build == None:
        return 'hg38'
    elif build.lower() in ('hg38', 'grch38'):
        return 'hg38'
    elif build.lower() in ('hg19', 'grch37'):
        return 'hg19'
    elif build.lower() in ('hg18', 'ncbi36'):
        return 'hg18'
    else:
        raise WrongRuntimeEnvironmentVariable(f'got unknown GWAS SS build: \"{build}\"')


def set_build(build) -> str:
    if build == None:
        return 'hg38'
    elif str(build).lower() in ('hg38', 'grch38', '38'):
        os.environ[GWASSS_BUILD_NUMBER_ENV] = 'hg38'
    elif str(build).lower() in ('hg19', 'grch37', '37'):
        os.environ[GWASSS_BUILD_NUMBER_ENV] = 'hg19'
    elif str(build).lower() in ('hg18', 'ncbi36', '36'):
        os.environ[GWASSS_BUILD_NUMBER_ENV] = 'hg18'
    else:
        raise WrongRuntimeEnvironmentVariable(f'got unknown GWAS SS build: \"{build}\"')

    return get_build()

