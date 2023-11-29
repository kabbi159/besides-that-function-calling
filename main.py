from openai import OpenAI

client = OpenAI()

stock_function = """namespace functions {

// Get the current stock price
type get_stock_price = (_: {
// The stock symbol
symbol: string,
}) => number;

} // namespace functions"""

stock_function_with_very_long_description = """
namespace functions {

// The "get_stock_price" function, residing within the "function" namespace, serves as a powerful tool for obtaining real-time stock price information. This function is designed to provide users with access to the current market value of a specific stock by accepting a "symbol" parameter, which represents the stock symbol or ticker symbol of the desired company or financial asset.
// By inputting the relevant stock symbol, users can leverage this function to retrieve accurate and up-to-date stock prices, allowing them to stay informed about the financial performance of their investments or assets. The function's simplicity and efficiency make it suitable for integration into various financial applications, trading platforms, or investment tools.
// In essence, the "get_stock_price" function enhances the accessibility of critical financial data, enabling users to make informed decisions in the dynamic world of stock markets. Whether for personal portfolio management or professional financial analysis, this function is a valuable resource for anyone seeking to monitor and react to market fluctuations effectively.
type get_stock_price = (_: {
// The stock symbol
symbol: string,
}) => number;

} // namespace functions
"""

weather_function = [
        {
            "name": "get_current_weather",
            "description": "Get the current weather in a given location",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The city and state, e.g. San Francisco, CA",
                    },
                    "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
                },
                "required": ["location"],
            },
        },
    ]

questions = ["What is the stock price of AAPL?", "What is the weather in San Francisco?"]

for question in questions:
    print(f"Question: {question}")
    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": stock_function_with_very_long_description},
        {"role": "user", "content": question},
    ],
    functions=weather_function,
    function_call="auto"
    )
    print()
    print(response)
    print()
