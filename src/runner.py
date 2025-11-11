thonimport json
from extractors.shopify_parser import ShopifyParser
from extractors.utils import load_settings, log_info

def run_scraper():
    log_info("Starting Shopify Scraper...")
    
    # Load settings from config
    settings = load_settings('src/config/settings.json')

    # Initialize the parser with settings
    parser = ShopifyParser(settings)
    
    # Run the scraper
    product_data = parser.scrape_products()

    # Save the result to a JSON file
    with open('data/sample.json', 'w') as f:
        json.dump(product_data, f, indent=4)
    
    log_info("Scraper run completed and data saved.")
    
if __name__ == "__main__":
    run_scraper()