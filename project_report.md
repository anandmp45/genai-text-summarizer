# Project Report: GenAI Text Summarizer

## 1. Abstract
The GenAI Text Summarizer is a simple web application that uses Generative Artificial Intelligence to convert long text into shorter, readable summaries. It is intended as an educational demonstration of how an AI model can be integrated into a software application.

## 2. Problem Statement
Reading lengthy articles, study notes, and informational documents can take considerable time. Users may need a shorter version that preserves the main ideas.

## 3. Objectives
- Build a simple interface for entering text.
- Connect the application to a Generative AI model through an API.
- Allow users to choose the summary format and length.
- Display and download the generated summary.

## 4. Tools and Technologies
| Tool / Technology | Purpose |
|---|---|
| Python | Application logic |
| Streamlit | Web user interface |
| Google Gemini API | Generative AI summarization |
| Google Gen AI Python SDK | API connection |
| Visual Studio Code / any code editor | Editing project files |

## 5. System Workflow
1. The user pastes text into the application.
2. The user chooses a summary style and length.
3. The application builds a prompt containing those choices and the source text.
4. The application sends the request to the Gemini API.
5. Gemini returns generated summary text.
6. The application displays the summary and provides a download option.

## 6. GenAI Integration
The project uses the Google Gen AI Python SDK. The API key is read from the `GEMINI_API_KEY` environment variable. The app sends the source text and instructions to the `gemini-2.5-flash` model. The model is instructed to preserve important facts and avoid inventing details.

## 7. Sample Input
Renewable energy comes from sources that are naturally replenished, such as sunlight, wind, water, and geothermal heat. Solar panels convert sunlight into electricity, while wind turbines use moving air to generate power.

## 8. Illustrative Output
- Renewable energy comes from naturally replenished sources such as sunlight, wind, water, and geothermal heat.
- Solar panels and wind turbines convert natural energy into electricity.

This output is illustrative. A live response is produced when the app is run with a valid API key.

## 9. Advantages
- Saves time when reviewing long text.
- Offers multiple summary formats.
- Provides a simple interface.
- Demonstrates practical API integration.

## 10. Limitations
- Requires an internet connection and valid API key.
- AI summaries may omit context or make mistakes.
- Very large inputs may exceed model or API limits.
- Users should verify important information against the original source.

## 11. Future Enhancements
- Upload PDF and DOCX files.
- Support multiple languages.
- Add summary history and user accounts.
- Add citation-aware summaries.

## 12. Conclusion
The GenAI Text Summarizer demonstrates how Generative AI can be integrated into a Python web application. It combines a user-friendly interface with an AI API to generate summaries in different formats and lengths.
