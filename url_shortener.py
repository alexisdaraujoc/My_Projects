import pyshorteners 

def shorten_url(url):
    # Create an instance of the URL Shortener
    s = pyshorteners.Shortener()

    # Shorten the URL
    shortened_url = s.tinyurl.short(url)

    # Return the shortened URL
    return shortened_url

# Prompt the user to enter a URL
url = input("Enter a URL: ")

# Call the function to shorten the URL
shortened_url = shorten_url(url)

# Print the shortened URL
print("Shortened URL:", shortened_url)