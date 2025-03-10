## Setting up Great Expectations

### Initialize Great Expectations:

Navigate to the great_expectations/ directory: cd great_expectations
Run great_expectations init to initialize Great Expectations.
Follow the prompts to configure Great Expectations. For now, you can choose the default options.
Great Expectations will create a great_expectations/great_expectations.yml file and other necessary directories.

Connect to Data Source:
Great Expectations needs to connect to your data source (PostgreSQL, or DuckDB).
Run great_expectations datasource new to create a new data source.
Choose the appropriate data source type (SQL for PostgreSQL, or DuckDB).
Configure the connection details (host, port, user, password, database, etc.).
Great Expectations will create a new data source configuration in great_expectations/datasources/.

Create Expectations:
Run great_expectations checkpoint new to create a new checkpoint.
A checkpoint is a configuration that runs one or more expectations suites.
Great Expectations will guide you through the process of creating an expectation suite.
You can add expectations to your suite using the Great Expectations UI or by editing the expectation suite JSON file directly.
For the example_bronze_model, create a simple expectation that the id column is not null.
Great expectations will create a .json file in the great_expectations/expectations/ directory.

Create a Checkpoint:
When creating the checkpoint, it will ask you which expectation suite to use, and which data to validate.
Great expectations will create a .yml file in great_expectations/checkpoints/.

Run Checkpoint:
Run great_expectations checkpoint run <checkpoint_name> to run the checkpoint and validate your data.
