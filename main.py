import urllib.request
import json
import sys

def get_random_fact():
    """
    Fetches a random useless fact from an external API.
    Demonstrates how to integrate with a free public API.
    """
    # This is a free, public API that provides random facts.
    # No API key or authentication is required, making it ideal for quick demos.
    api_url = "https://uselessfacts.jsph.pl/random.json?language=en"
    try:
        # Make an HTTP GET request to the API endpoint using Python's standard library.
        with urllib.request.urlopen(api_url) as response:
            # Read the response body, which is expected to be JSON.
            data = response.read().decode("utf-8")
            # Parse the JSON response into a Python dictionary.
            fact_data = json.loads(data)

            # Extract the 'text' field, which contains the actual fact.
            # Using .get() provides a default value if the key is missing.
            fact_text = fact_data.get("text", "No fact found.")
            return fact_text
    except urllib.error.URLError as e:
        # Handle network-related errors (e.g., no internet connection, invalid URL).
        print(f"Error fetching fact: {e.reason}", file=sys.stderr)
        return "Could not fetch a fact. Please check your internet connection."
    except json.JSONDecodeError:
        # Handle errors if the API response is not valid JSON.
        print("Error decoding JSON response from API.", file=sys.stderr)
        return "Could not decode API response."
    except Exception as e:
        # Catch any other unexpected errors.
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        return "An unexpected error occurred."

if __name__ == "__main__":
    print("Fetching a random fact for your side project inspiration...")
    fact = get_random_fact()
    print("\n--- Your Random Fact ---")
    print(fact)
    print("------------------------")
    print("\nThis demonstrates how to use a free API to get data for your projects.")
