.PHONY: test install pep8 release clean doc

test: pep8
	py.test -v --cov={{cookiecutter.source}} -l --tb=short tests/ -vv

install:
	python setup.py develop

pep8:
	@flake8 {{cookiecutter.source}} --ignore=F403

release: test
	@python setup.py sdist bdist_wheel upload

clean:
	@find ./ -name '*.pyc' -exec rm -f {} \;
	@find ./ -name 'Thumbs.db' -exec rm -f {} \;
	@find ./ -name '*~' -exec rm -f {} \;