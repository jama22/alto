# Alto Function
Main goal is to see if you can just describe a script and deploy it onto GCF. Looks like you can:

- `main.py` holds all the functions
- `templates/` interestingly, you can tell the function to grab a file and the framework knows how to get it

Notably I separated this sub-project out into its own set of `requirements` because it uses GCF's `framework-functions` Python package