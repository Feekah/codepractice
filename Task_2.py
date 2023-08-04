#Library Imports
import requests         #The requests library is needed to make HTTP requests e.g. GET requests for API interaction
import pandas as pd     #The pandas library will be used to make the input excel file usable by the python environment.
import os               #The os library is used for writing/saving files to the system

#Functions Definition

#Function 1: Calling the Namsor API
#The function takes in the first and last name from the main function
def call_namsor_api(first_name, last_name):
    #This URL is the GET url for requesting Diaspora information, obtained from the site: https://namsor.app/api-documentation#name-diaspora-batch
    api_url = f"https://v2.namsor.com/NamSorAPIv2/api2/json/diaspora/GBR/{first_name}/{last_name}"

    #API key retrieved from website
    headers = {
        "X-API-KEY": "997039c95bd4d8ad3e665ee097a8b6d8"
    }

    #Use the GET function to access the api_url taking in the API key
    response = requests.get(api_url, headers=headers)

    #Return the json formatted ethnicity and ethnicityAlt for each name
    return response.json()

#Function 2: The main function
def main():
    #define the input and output file paths
    input_file = "Names_List.xlsx"
    output_folder = "output/"

    #Load the input file, specify the sheet containing the names: Sheet3
    name_list = pd.read_excel(input_file, sheet_name='Sheet3')

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    #Parse through the names using a for loop
    for index, row in name_list.iterrows():

        #map the first name to the variable 'first_name'
        first_name = row["First Name"]

        #map the last name to the variable 'last_name'
        last_name = row["Last Name"]

        #Call the Namsor API function and assign the output to 'response'
        response = call_namsor_api(first_name, last_name)

        # Extract ethnicity and alternate ethnicity values from the response
        ethnicity = response.get("ethnicity", "")
        ethnicity_alt = response.get("ethnicityAlt", "")

        #Update the DataFrame with ethnicity and alternate ethnicity values
        name_list.at[index, "Ethnicity"] = ethnicity
        name_list.at[index, "Alternate Ethnicity"] = ethnicity_alt

        # Save API response to a file
        output_filename = os.path.join(output_folder, f"{first_name}_{last_name}.txt")
        with open(output_filename, "w", encoding="utf-8") as output_file:
            output_file.write(str(response))

    # Save the updated DataFrame back to the Excel file, with no indexing.
    name_list.to_excel("Updated_Names_List.xlsx", index=False, engine="openpyxl")

#Execute the main function when the program is run
if __name__ == "__main__":
    main()