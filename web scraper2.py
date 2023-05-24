import requests
from bs4 import BeautifulSoup

# Get user input for the website link
link = input("Enter the website link to scrape: ")
try:
    # Send an HTTP GET request to the website
    response = requests.get(link)

    # Get the HTML content from the response
    html_content = response.content

    # Create a BeautifulSoup object with the 'html.parser' parser
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find the element based on its attributes
    div_element = soup.find("div", class_="caption")

    # Example: Extracting the price from a span element with a specific class
    # Extract the desired information
    if div_element:
        price_element = div_element.find("h4", class_="pull-right-price")
        title_element = div_element.find("a", class_="title")
        description_element = div_element.find("p", class_="description")
        if price_element:
            price = price_element.get_text().strip()
            print("Price:", price)

        if title_element:
            title = title_element.get_text().strip()
            print("Title:", title)

        if description_element:
            description = description_element.get_text().strip()
            print("Description:", description)
        else:
            print("Element not found.")

    # Prettify the HTML content
    prettified_html = soup.prettify()
    # Save the HTML content to a file
    with open("website_content.html", "w", encoding="utf-8") as file:
        file.write(prettified_html)
        print("HTML file created: website_content.html")

    # Find and print the title
    title = soup.title
    if title:
        print("Page Title:", title.text)
    else:
        print("Title not found.")

except requests.exceptions.RequestException as e:
    print("An error occurred while making the request:", e)