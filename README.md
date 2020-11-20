# Raw Data Converter
(20 Nov 2020)

A simple python script that reads an excel file and:
* **Adds "+63" prefix** from phone numbers column,
* **Extracts last names** from the full names column, and
* **Calculates Cash On Delivery (COD)** based on location, weight, and parcel value.

Outputs are inside the created _converted-name_phone.xlsx_ and _converted-cod.xlsx_.

### Getting Started
1. Install [Python](https://www.python.org/) and `pip` if your computer does not have both.

    ```bash
    # To check if python and pip is installed, type
    $ python --version  # Should output your python version ex:
    # Python 3.8.6
    $ pip --version  # Should output your pip version ex:
    # pip 20.2.
    ```

2. Clone the repository and cd into the cloned folder. If you do not have _git_, download the repository and extract the files.

    ```bash
    $ git clone https://github.com/MREstepa/data-converter.git
    $ cd data-converter
    ```

3. Install `requirements.txt` by using pip.

    ```
    $ pip install requirements.txt
    ```

4. Edit the `converter-feed.xlsx` excel file and place your raw data in the designated columns.

5. Run the python script.

    ```
    $ python data-converter.py
    ```
    
6. Outputs will be inside the created excel files: `converted-name_phone.xlsx` and/or `converted-cod.xlsx`, depending on which process you picked.

_____

MREstepa
