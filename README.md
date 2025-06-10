# AI Cover Letter Generator

This project provides a convenient way to generate tailored cover letters using an AI model. By supplying your resume and a job description URL, the script extracts key requirements from the job posting and crafts a personalized cover letter.

## Features

* **Job Description Analysis:** Automatically identifies important details like role requirements, education, and years of experience from a provided job description URL.
* **Resume Integration:** Incorporates information from your resume to create a highly relevant cover letter.
* **AI-Powered Generation:** Leverages a powerful language model to draft professional and customized cover letters.

## Prerequisites

Before you begin, ensure you have the following installed:

* **Python 3.8+**
* **pip** (Python package installer)

You will also need a **Groq API Key**.

## Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/kzxjg/Cover-Letter-Generator.git
    ```

2.  **Install the required Python packages:**

    ```bash
    pip install -r requirements.txt
    ```

    ```
    langchain-groq
    langchain-core
    langchain-community
    python-docx
    ```

## Usage

1.  **Set your Groq API Key:**
    When you run the script for the first time, it will prompt you to enter your Groq API key. Alternatively, you can set it as an environment variable:

    ```bash
    export GROQ_API_KEY="your_groq_api_key_here"
    ```

    (Replace `"your_groq_api_key_here"` with your actual key.)

2.  **Run the script:**

    ```bash
    python your_script_name.py <path_to_your_resume.docx> <job_description_url>
    ```

    * Replace `<path_to_your_resume.docx>` with the actual path to your resume file (e.g., `my_resume.docx`).
    * Replace `<job_description_url>` with the direct URL of the job description you're applying for.

    **Example:**

    ```bash
    python generate_cover_letter.py my_resume.docx "[https://example.com/job-postings/software-engineer](https://example.com/job-postings/software-engineer)"
    ```

    The generated cover letter will be printed to your console.

## How it Works

The script performs the following steps:

1.  **Loads Arguments:** Takes your resume file path and the job description URL as command-line arguments.
2.  **Loads Job Description:** Uses `WebBaseLoader` to fetch and parse the content from the provided job description URL.
3.  **Loads Resume:** Reads your resume content from the specified `.docx` file using `python-docx`.
4.  **Extracts Job Details:** Employs an AI model (via `ChatGroq`) to identify and extract key requirements from the job description.
5.  **Generates Cover Letter:** Feeds the extracted job details and your resume content to another AI prompt to generate a personalized cover letter.
6.  **Outputs Cover Letter:** Prints the final cover letter to your console.

## Contributing

We welcome contributions! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.

## License

This project is open-source and available under the [MIT License](LICENSE).

---
