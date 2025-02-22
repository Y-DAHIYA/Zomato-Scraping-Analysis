# Import Python libraries
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# List to hold restaurant URLs
Urls = []

def scrape_zomato_delivery_data(url, output_file):
    """
    Scrapes restaurant delivery data from Zomato and saves it to a CSV file.

    Parameters:
        url (str): The URL of the Zomato page to scrape.
        output_file (str): The path to the CSV file where the data will be saved.
    """


    # Initialize the Chrome WebDriver
    driver = webdriver.Chrome()      # Launch Goggle Chrome for Scraping
    try:

        # Open the provided URL
        driver.get(url)        # Load the Page
        SCROLL_PAUSE_TIME = 10     # Time to wait between scroll


        # Get the intial height of the page for scrolling
        last_height = driver.execute_script("return document.body.scrollHeight")


        # Continuously scroll down the page to load all dynamic content
        while True:
            # Scroll to the bottom of the page
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            # Wait for the new content to load
            time.sleep(SCROLL_PAUSE_TIME)
            # Check the new height
            new_height = driver.execute_script("return document.body.scrollHeight")
            # If no new content is loaded, stop scrolling
            if new_height == last_height:
                break
            # Update last_height to new_height for the next scroll
            last_height = new_height


        # Initialize lists to hold data
        Restaurant_Names = []
        Ratings = []
        Cuisine_Types = []
        Cost_for_Ones = []
        Delivery_Times = []
        OFF_offers = []
        Url_links = []


        # Wait for card elements to be visible
        card_elements = WebDriverWait(driver, 20).until(
            EC.visibility_of_all_elements_located((By.CSS_SELECTOR, '.sc-kDgGX.fjYwDL'))
        )


        # Loop through extract data from each card element
        for card in card_elements:

            try:
                # Extract the Offers & Append "NA" if no offer is available
                OFF_offers.append(card.find_element(By.CSS_SELECTOR, '.sc-1hez2tp-0.sc-hPeUyl.kxuuMh').text)
            except:
                OFF_offers.append("NA")


            try:
                # Extract the Restaurant Url & Append "NA" if no URL is available
                Url_links.append(card.find_element(By.CSS_SELECTOR, 'a.sc-gLdKKF.kSLcCi').get_attribute("href"))
            except:
                Url_links.append("NA")


            try:
                # Extract the Restaurant Name & Append "NA" if no name is available
                Restaurant_Names.append(card.find_element(By.CSS_SELECTOR, 'h4.sc-1hp8d8a-0.sc-lXiCt.hoNwWu').text)
            except:
                Restaurant_Names.append("NA")


            try:
                # Extract the Rating & Append "NA" if no rating is available
                Ratings.append(card.find_element(By.CSS_SELECTOR, 'div.sc-1q7bklc-1.cILgox').text)
            except:
                Ratings.append("NA")


            try:
                # Extract the Cuisine Type & Append "NA" if no cuisine type is available
                Cuisine_Types.append(card.find_element(By.CSS_SELECTOR, '.sc-1hez2tp-0.sc-dcOKER.zafot').text)
            except:
                Cuisine_Types.append("NA")


            try:
                # Extract the Cost & Append "NA" if no cost data is available
                Cost_for_Ones.append(card.find_element(By.CSS_SELECTOR, '.sc-1hez2tp-0.sc-dcOKER.imYCjj').text)
            except:
                Cost_for_Ones.append("NA")


            try:
                # Extract the Delivery Time & Append "NA" if no delivery time is available
                Delivery_Times.append(card.find_element(By.CSS_SELECTOR, 'div.min-basic-info-right').text)
            except:
                Delivery_Times.append("NA")


        # Add the URL links to the global list
        Urls.extend(Url_links)


        # Ensure all lists have the same length
        min_length = min(len(Restaurant_Names), len(Ratings), len(Cuisine_Types),
                         len(Cost_for_Ones), len(Delivery_Times), len(OFF_offers), len(Url_links))


        # Trim lists to the same length
        Restaurant_Names = Restaurant_Names[:min_length]
        Ratings = Ratings[:min_length]
        Cuisine_Types = Cuisine_Types[:min_length]
        Cost_for_Ones = Cost_for_Ones[:min_length]
        Delivery_Times = Delivery_Times[:min_length]
        OFF_offers = OFF_offers[:min_length]
        Url_links = Url_links[:min_length]


        # Create a DataFrame and save to CSV
        df = pd.DataFrame({
            "Restaurant_Name": Restaurant_Names,
            "Rating": Ratings,
            "Cuisine_Type": Cuisine_Types,
            "Cost_for_One": Cost_for_Ones,
            "Delivery_Time": Delivery_Times,
            "OFF_offer": OFF_offers,
            "Url_link": Url_links
        })
        df.to_csv(output_file, index=False)       # Save the DataFrame to the specified output file
        print(f"DataFrame saved to {output_file}")     # Confirmation message


    except Exception as e:
        # Print error message if an exception occurs
        print(f"Error during scraping: {e}")


    finally:
        # Close the browser window
        driver.quit()


def scrape_zomato_reviews(review_urls, output_file):
    """
    Scrapes reviews from Zomato using the provided review URLs and saves them to a CSV file.

    Parameters:
        review_urls (list of str): List of review URLs to scrape.
        output_file (str): Path to the CSV file where the review data will be saved.
    """


    # Initialize the Chrome WebDriver
    driver = webdriver.Chrome()      # Launch Chrome browser for scraping reviews


    # Lists to hold review data
    names = []
    reviews = []
    followers = []
    stars = []
    times = []
    votes = []
    comments = []
    types = []


    try:

        # Loop through each review URL provided
        for url in review_urls:
            try:
                # Open each review URL
                driver.get(url)
                time.sleep(3)  # Wait for the page to load & Adjust sleep time as needed


                # Loop through multiple pages of reviews
                for _ in range(10):  # Number of pages to scrape
                    try:
                        # Locate the container with review data
                        containers = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/section[4]/div/div/section/div[2]')


                        # Extract individual review data
                        names_elements = containers.find_elements(By.CSS_SELECTOR, "p")
                        reviews_elements = containers.find_elements(By.CSS_SELECTOR, 'span')
                        stars_elements = containers.find_elements(By.CSS_SELECTOR, 'div[class="sc-1q7bklc-1 cILgox"]')
                        times_elements = containers.find_elements(By.CSS_SELECTOR, 'p[class="sc-1hez2tp-0 fKvqMN time-stamp"]')
                        votes_elements = containers.find_elements(By.CSS_SELECTOR, 'p[class="sc-1hez2tp-0 fKvqMN"]')
                        comments_elements = containers.find_elements(By.CSS_SELECTOR, 'p')
                        types_elements = containers.find_elements(By.CSS_SELECTOR, 'div[class="sc-1q7bklc-9 dYrjiw"]')


                        # Append data to lists
                        names += [element.text for j, element in enumerate(names_elements) if j % 4 == 0]
                        reviews += [element.text for j, element in enumerate(reviews_elements) if j % 7 == 0]
                        followers += [element.text for j, element in enumerate(reviews_elements) if j % 7 == 1]
                        stars += [element.text for element in stars_elements]
                        times += [element.text for element in times_elements]
                        votes += [element.text for element in votes_elements]
                        comments += [element.text for j, element in enumerate(comments_elements) if j % 4 == 2]
                        types += [element.text for element in types_elements]


                        # Find and click the 'Next' button to go to the next page of reviews
                        try:

                            next_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/section[4]/div/div/section/div[3]/div[2]/div/a[6]')
                            next_button.click()   # Click to navigate to the next page
                            time.sleep(5)    # Wait for the next page to load

                        except:

                            print("No more pages or error navigating to next page.")
                            break  # Exit loop if 'Next' button is not found (i.e., no more pages)


                    except Exception as e:
                        print(f"Error processing review page: {e}")
                        break    # Exit loop if review container is not found


            except Exception as e:
                print(f"Error with URL {url}: {e}")
                continue


        # Ensure all lists have the same length
        min_length = min(len(names), len(reviews), len(followers), len(stars), len(times), len(votes), len(comments), len(types))


        # Trim lists to the same length
        names = names[:min_length]
        reviews = reviews[:min_length]
        followers = followers[:min_length]
        stars = stars[:min_length]
        times = times[:min_length]
        votes = votes[:min_length]
        comments = comments[:min_length]
        types = types[:min_length]


        # Create a DataFrame and save to CSV
        df = pd.DataFrame({
            "Customer_name": names,
            "Number_of_Reviews": reviews,
            "Number_of_Followers": followers,
            "Star_Rating": stars,
            "Time_of_Posting": times,
            "Votes_&_Comments": votes,
            "Review_Text": comments,
            "Type": types
        })
        df.to_csv(output_file, index=False)     # Save the DataFrame to the specified output file
        print(f"DataFrame saved to {output_file}")    # Confirmation message


    except Exception as e:
        # Print error message if an exception occurs
        print(f"Error during scraping: {e}")


    finally:
        # Close the browser window
        driver.quit()     


# Run the scraping functions
scrape_zomato_delivery_data("https://www.zomato.com/bangalore/delivery", 'zomato_data.csv')
review_urls = [url.replace('/order', '/reviews') for url in Urls]
scrape_zomato_reviews(review_urls[0:2], 'zomato_reviews.csv')
