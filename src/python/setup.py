from pathlib import Path
from zensols.pybuild import SetupUtil

su = SetupUtil(
    setup_path=Path(__file__).parent.absolute(),
    name="zensols.propbankdb",
    package_names=['zensols', 'resources'],
    package_data={'': ['*.conf', '*.json', '*.yml', '*.sql']},
    description='An API to access the PropBank database and generate embeddings from them.',
    user='plandes',
    project='propbankdb',
    keywords=['tooling'],
).setup()
