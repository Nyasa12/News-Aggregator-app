# 📰 News Aggregator App

## Overview

News Aggregator is a simple Python-based desktop application that allows users to search for the latest news articles on any topic. The application fetches real-time news data using the NewsAPI service and displays the latest headlines along with their article links in an easy-to-use graphical interface.

## Features

* Search news by keyword or topic.
* Fetches latest news articles in real time.
* Displays top 5 recent news headlines.
* Provides direct article links.
* User-friendly graphical interface built with Tkinter.
* Error handling for invalid searches and API issues.

## Technologies Used

* Python
* Tkinter (GUI Development)
* Requests Library (API Communication)
* NewsAPI

## Project Structure

* **Tkinter GUI** for user interaction.
* **NewsAPI Integration** to retrieve news data.
* **Text Widget** to display headlines and URLs.
* **Exception Handling** to manage API and network errors.

## How It Works

1. The user enters a topic in the search box.
2. When the "Get News" button is clicked, the application sends a request to NewsAPI.
3. The API returns the latest articles related to the entered topic.
4. The application extracts the title and URL of each article.
5. The top 5 news articles are displayed in the output section.

## Requirements

Install the required package:

```bash
pip install requests
```

## API Configuration

Create an account on NewsAPI and generate your API key.

Replace the API key in the code:

```python
API_KEY = "YOUR_API_KEY"
```

## Running the Application

```bash
python news_aggregator.py
```

## Future Enhancements

* Open news articles directly in a web browser.
* Category-based news filtering.
* Save news articles for offline reading.
* Dark mode support.
* News source selection feature.

## Conclusion

The News Aggregator App demonstrates the integration of APIs with Python GUI development. It provides users with quick access to the latest news on any topic through a simple and interactive desktop application.
