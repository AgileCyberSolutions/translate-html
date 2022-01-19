README

This library is used to translate the html file to the destination langauge


1. Prerequisites:

    python (3.8.10)


2. Installation:

    1. Create python virtual Environment and Activate it in your machine.
    
        For ubuntu 

        python3 -m venv my-project-env

        source my-project-env/bin/activate

    2. Clone the package and placed the files in the folder(my-project-env)

    3. Run the below command from the project's root directory((my-project-env))

        pip install -r requirements.txt [To install the required modules]
    

3. To run the program:

    Sample html file need to placed in the project directory. [In our project "test.html"]
    Run the command 

    python translate_html.py
    
    Now you can see the Output.html ['The newly translated html file'] in the project directory.


4. Customize The Language Locale Codes variable:

    language_locale = "ca" [You can change this locale to another]

5. Limitations of the Google Trans library:

    [Since it uses the web API of translate.google.com It has some limitations]:

    1. The maximum character limit on a single text is 15k
    2. If you get HTTP 5xx error or errors like #6, it's probably because Google has banned your client IP address.
    3. Due to limitations of the web version of google translate, translate.google.com API does not guarantee that the library would work properly at all times (so please use this library if you don't care about stability).
