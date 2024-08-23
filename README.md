# IRIDA Metadata Uploader

Python program for uploading metadata to [IRIDA](https://github.com/phac-nml/irida)

For NGS data uploads, see [IRIDA Uploader](https://github.com/phac-nml/irida-uploader/)

This projects code has been adapted from the much larger [ARTIC Nextflow pipeline project](https://github.com/phac-nml/ncov2019-artic-nf)

## Run from source code

```bash
make
source .virtualenv/bin/activate
irida-metadata-uploader --help
```

### Running the metadata uploader

Usage
```bash
usage: irida-metadata-uploader [-h] -c CONFIG -m METADATA_CSV [--no_sample_creation]
```

#### CONFIG

Specify a config file for connection to IRIDA. This is identical to an IRIDA Uploader config file.

[Click here for more infomation about this file](https://irida-uploader.readthedocs.io/en/stable/configuration.html)

#### METADATA_CSV

Table must be in CSV format and must contain `sample` and `project_id` as the first 2 columns. All other columns will be processed as metadata.

Example table:

|    sample    | project_id | sequencing_technology |    date    |   favourite_food  |
|:------------:|:----------:|:---------------------:|:----------:|:-----------------:|
|  SR21-0010f  |      3     |         MiSeq         | 2021-04-12 |        Cake       |
|   CoV-20111  |     12     |        GridION        | 2021-06-09 |     Ice:Cream     |
| R3332-fad-34 |     23     |         MinION        | 2021-05-16 | Cookies are great |

Example as CSV

```csv
sample,project_id,sequencing_technology,date,favourite_food
SR21-0010f,3,MiSeq,2021-04-12,Cake
CoV-20111,12,GridION,2021-06-09,Ice:Cream
R3332-fad-34,23,MinION,2021-05-16,Cookies are great
```

##### Note: Any empty columns will be filled with `"NA"`

#### --no_sample_creation (optional)

Turns off sample creation for sample names not found in IRIDA