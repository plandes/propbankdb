# PropBank Database and Embeddings

[![PyPI][pypi-badge]][pypi-link]
[![Python 3.11][python311-badge]][python311-link]
[![Build Status][build-badge]][build-link]

An API to access [PropBank] data and generate embeddings from the paper
[CALAMR: Component ALignment for Abstract Meaning Representation] used by the
[zensols.calamr] repository.  This creates a database and generates embeddings
from [PropBank frameset files] and makes it available as n API that attempts to
reduce the data complexity of the [PropBank] using an object oriented Pythonic
approach.  It will automatically download a [distribution file] that contains:

* An SQLite relational normalized database,
* [Sentence-BERT] [embeddings] for role sets, roles and functions,
* A CSV file with the corresponding extracted sentences used for the
  embeddings,
* A metadata file containing version information and bindings for the
  embeddings used by the [Zensols framework].

The API binds the relational data from the SQLite database with simple, but
performant object mappings in Python while allowing a direct row/cursor based
access to the data using the [Zensols Dbutil] API.

If you use this library or the [zensols.calamr] API, please [cite](#citation)
our paper.


## Documentation

See the [full documentation](https://plandes.github.io/propbankdb/index.html).
The [API reference](https://plandes.github.io/propbankdb/api.html) is also
available.


## Obtaining

The library can be installed with pip from the [pypi] repository:
```bash
pip3 install zensols.propbankdb
```


## Embeddings and Database

A [PropBank] database with SentenceBERT embeddings for the paper CALAMR:
Component ALignment for Abstract Meaning Representation.  This is used by the
zensols.propbankdb Python API but can be used on its own as well.  The database
contains roles, rolesets and other PropBank data along with their examples,
descriptions, functions etc. embeddings.  See the API repository for more
information.

[Sentence-BERT] embeddings are available for the following [PropBank frameset
files] XML fields:

* Role set names (`name` attribute)
* Role descriptions (`descr` attribute)
* Function description (defined in the `.dtd` file from [PropBank frameset
  files] repository)

The models and the SQLite [PropBank] database are automatically downloaded on
the first use of the command-line tool or API.  However, they can also be
[downloaded](https://zenodo.org/records/10806450) directly.


## Usage

The installed software can be used to look up data from the command line, but
was designed to be used as an API for data access and embeddings.


### Command Line

The command line details are available with the command line help using:

```bash
$ propbankdb --help
```

For example, to get the `see.01` role set in JSON format use:
```bash
$ propbankdb roleset -f json see.01
```

### API

Access a role set and its embedding from the database:
```python
from zensols.propbankdb import Roleset, Database, ApplicationFactory
db: Database = ApplicationFactory.get_database()
rs: Roleset = db.roleset_stash['see.01']
# print out the rule set, the number of roles it has, and embedding shape
print(rs, len(rs.roles), rs.embedding.shape)
>>> see.01: view 3 torch.Size([768])
# print the roleset information
rs.write()
>>> id:
>>>     label: see.01
>>>     lemma: see
>>>     index: 1
>>> name: view
>>> aliases:
>>>     part_of_speech: PartOfSpeech.verb
>>>     word: see
>>>     part_of_speech: PartOfSpeech.noun
>>>     word: seeing
>>>     part_of_speech: PartOfSpeech.verb
>>>     word: sight
>>>     part_of_speech: PartOfSpeech.noun
>>>     word: sight
>>> roles:
>>>     description: viewer
>>>     function:
>>>         label: PAG
>>>         description: prototypical agent
>>>         group: default
...
```

The [roleshow.py](example/roleshow.py) example shows how to use your own
application context as a minimum example providing only data access.  The
[role-with-embedding.py](example/role-with-embedding.py) example adds more
resource libraries necessary to fetch embeddings.


### Training

Use the `dist.py` script to train new embeddings and recreate the database:
1. Edit the `transformer_sent_fixed_resource` section `model_id` in the
   [configuration file](deploy-resources/obj.yml) to use different embeddings
1. Start with a clean environment: `./dist.py clean`
1. Create the distribution: `./dist.py package`


## Citation

If you use this project in your research please use the following BibTeX entry:

```bibtex
@inproceedings{landesCALAMRComponentALignment2024,
  title = {{{CALAMR}}: {{Component ALignment}} for {{Abstract Meaning Representation}}},
  booktitle = {The 2024 {{Joint International Conference}} on {{Computational Linguistics}}, {{Language Resources}} and {{Evaluation}}},
  author = {Landes, Paul and Di Eugenio, Barbara},
  date = {2024-05-20},
  publisher = {International Committee on Computational Linguistics},
  location = {Turin, Italy},
  eventtitle = {{{LREC-COLING}} 2024}
}
```


## Changelog

An extensive changelog is available [here](CHANGELOG.md).


## Community

Please star this repository and let me know how and where you use this API.
Contributions as pull requests, feedback and any input is welcome.


## License

[MIT License](LICENSE.md)

Copyright (c) 2023 - 2025 Paul Landes


<!-- links -->
[pypi]: https://pypi.org/project/zensols.propbankdb/
[pypi-link]: https://pypi.python.org/pypi/zensols.propbankdb
[pypi-badge]: https://img.shields.io/pypi/v/zensols.propbankdb.svg
[python311-badge]: https://img.shields.io/badge/python-3.11-blue.svg
[python311-link]: https://www.python.org/downloads/release/python-3110
[build-badge]: https://github.com/plandes/propbankdb/workflows/CI/badge.svg
[build-link]: https://github.com/plandes/propbankdb/actions

[PropBank]: https://propbank.github.io
[propbank frameset files]: https://github.com/propbank/propbank-frames
[Zensols framework]: https://github.com/plandes/deepnlp
[Zensols Dbutil]: https://github.com/plandes/dbutil
[configuration]: https://plandes.github.io/util/doc/config.html
[embeddings]: #embeddings
[Sentence-BERT]: https://arxiv.org/abs/1908.10084
[CALAMR: Component ALignment for Abstract Meaning Representation]: https://example.com
[zensols.calamr]: https://github.com/plandes/calamr
[Zenodo]: https://zenodo.org/records/10806450
