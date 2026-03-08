# How to Setup Project

1. Install `uv` (a fast Python package installer and resolver) with the following command:
   ```powershell
   powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
   ```

2. Initialize the project using `uv`:
   ```powershell
   uv init
   ```
   **What this does (for beginners):** 
   The `uv init` command sets up a new Python project in your current folder. It automatically creates a standard starting structure for you, which typically includes:
   - A `pyproject.toml` file: This is the main configuration file where your project's details and dependencies (other packages your project needs) will be saved.
   - A `.python-version` file: This pins the specific version of Python your project uses, ensuring everyone working on it uses the same version.
   - A basic Python script (like `hello.py`) to give you a working starting point.

3. Add the `langchain` package to your project:
   ```powershell
   uv add langchain
   ```
   **What this does (for beginners):**
   The `uv add` command downloads the `langchain` library (and any other packages it depends on) from the internet and installs it into your project's isolated environment. It also automatically updates your `pyproject.toml` and `uv.lock` files to record that your project requires `langchain`. This ensures that anyone else who runs your code can easily install the exact same packages.

4. Add the `langchain-google-genai` package to use Gemini:
   ```powershell
   uv add langchain-google-genai
   ```
   **What this does (for beginners):**
   This command installs the specific Langchain integration for Google's GenAI (Gemini) models. Because Langchain is built to work with many different AI providers, they separate the core library from the provider-specific integrations. You need this package to connect Langchain to Gemini.

5. Add the `python-dotenv` package to manage environment variables:
   ```powershell
   uv add python-dotenv
   ```
   **What this does (for beginners):**
   When building apps with AI, you'll need API keys (like a password for Gemini). It's very dangerous to put these directly in your code because if you share your code, others will see your secret keys. `python-dotenv` lets you store these secrets safely in a separate hidden file (called `.env`). It then automatically loads these hidden secrets into your code when it runs.

6. Add the `black` and `isort` packages to format your code automatically:
   ```powershell
   uv add black isort
   ```
   **What this does (for beginners):**
   `black` and `isort` are tools that help keep your Python code clean and organized. 
   - `black` automatically formats your code to follow standard Python style guidelines (like adding the right spaces and quotes).
   - `isort` specifically sorts the `import` statements at the top of your files alphabetically and groups them logically. 
   Using these tools saves you time manually formatting code and avoids arguments about styling when collaborating with others!

7. Create your main application file `main.py` and write your initial code:
   ```python
   import os
   from langchain_core.prompts import PromptTemplate
   from dotenv import load_dotenv

   from langchain_google_genai import ChatGoogleGenerativeAI
   load_dotenv()


   def main():
       print("Hello from practice!")
       print(os.getenv("GOOGLE_API_KEY"))
       information = """
       Elon Reeve Musk (/ˈiːlɒn/ EE-lon; born June 28, 1971) is a businessman and entrepreneur known for his leadership of Tesla, SpaceX, X, and xAI. Musk has been the wealthiest person in the world since 2025; as of February 2026, Forbes estimates his net worth to be around US$852 billion.

   Born into a wealthy family in Pretoria, South Africa, Musk emigrated in 1989 to Canada; he has Canadian citizenship since his mother was born there. He received bachelor's degrees in 1997 from the University of Pennsylvania before moving to California to pursue business ventures. In 1995, Musk co-founded the software company Zip2. Following its sale in 1999, he co-founded X.com, an online payment company that later merged to form PayPal, which was acquired by eBay in 2002. Musk also became an American citizen in 2002.

   In 2002, Musk founded the space technology company SpaceX, becoming its CEO and chief engineer; the company has since led innovations in reusable rockets and commercial spaceflight. Musk joined the automaker Tesla as an early investor in 2004 and became its CEO and product architect in 2008; it has since become a leader in electric vehicles. In 2015, he co-founded OpenAI to advance artificial intelligence (AI) research, but later left; growing discontent with the organization's direction and leadership in the AI boom in the 2020s led him to establish xAI, which became a subsidiary of SpaceX in 2026. In 2022, he acquired the social network Twitter, implementing significant changes, and rebranding it as X in 2023. His other businesses include the neurotechnology company Neuralink, which he co-founded in 2016, and the tunneling company the Boring Company, which he founded in 2017. In November 2025, a Tesla pay package worth $1 trillion for Musk was approved, which he is to receive over 10 years if he meets specific goals.

   Musk was the largest donor in the 2024 U.S. presidential election, where he supported Donald Trump. After Trump was inaugurated as president in early 2025, Musk served as Senior Advisor to the President and as the de facto head of the Department of Government Efficiency (DOGE). After a public feud with Trump, Musk left the Trump administration and returned to managing his companies. Musk is a supporter of global far-right figures, causes, and political parties. His political activities, views, and statements have made him a polarizing figure. Musk has been criticized for COVID-19 misinformation, promoting conspiracy theories, and affirming antisemitic, racist, and transphobic comments. His acquisition of Twitter was controversial due to a subsequent increase in hate speech and the spread of misinformation on the service, following his pledge to decrease censorship. His role in the second Trump administration attracted public backlash, particularly in response to DOGE. The emails he sent to Jeffrey Epstein are included in the Epstein files, which were published between 2025–26 and became a topic of worldwide debate.
       """
       summary_template="""
       Given the information {information} about a person i want you to create:
       1. A short summary
       2. Two intrestion fact about them
       """
       summary_prompt_template=PromptTemplate(input_variables=["information"],template=summary_template)
       llm=ChatGoogleGenerativeAI(model="gemini-2.5-flash",temperature=0.7)
       chain=summary_prompt_template|llm
       response=chain.invoke(input={"information":information})
       print(response.content)
       

   if __name__ == "__main__":
       main()
   ```

   **What this code does (Detailed Line-by-Line for Beginners):**

   *   **`import os`**: This gives Python access to your operating system's features, like reading environment variables such as your API keys.
   *   **`from langchain_core.prompts import PromptTemplate`**: Langchain makes working with AI easier. This specific tool (`PromptTemplate`) lets you create "templates" for your instructions to the AI. Think of it like a Mad-Libs worksheet where you have a static sentence with a blank `___` slot to fill in later.
   *   **`from dotenv import load_dotenv`**: This imports the function required to find and load our hidden `.env` secrets file.
   *   **`from langchain_google_genai import ChatGoogleGenerativeAI`**: This imports the module explicitly designed to let your code connect directly with Google's Gemini models using Langchain's standard format.
   *   **`load_dotenv()`**: This triggers the function that searches your folder for the `.env` file and securely loads your private keys (like `GOOGLE_API_KEY`) into memory so the application can use them.
   
   **(Inside the `main` function):**
   *   **`print("Hello from practice!")`**: A simple test print to verify the script is running successfully at the start.
   *   **`print(os.getenv("GOOGLE_API_KEY"))`**: Retrieves your secret key and prints it to the screen. *(Security Note: In a real-world application, you should never print your secrets out directly!)*
   *   **`information = """ ... """`**: We create a variable named `information` and assign it a massive block of text. The triple quotes (`"""`) allow us to format strings across multiple lines easily. This is the raw data we want the AI to analyze.
   *   **`summary_template = """ ... {information} ... """`**: This constructs the actual instruction prompt we will send to the AI. Notice the `{information}` part wrapped in curly braces? That acts as a variable placeholder slot.
   *   **`summary_prompt_template = PromptTemplate(input_variables=["information"], template=summary_template)`**: This step converts our text string into a smart Langchain `PromptTemplate` object. By defining `input_variables=["information"]`, we are explicitly telling Langchain what variable name needs to be supplied to fill in the curly braces.
   *   **`llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.7)`**: Here we define the "brain" of our operation (`llm` stands for Large Language Model). `model="gemini-2.5-flash"` tells Langchain to specifically boot up Google's Gemini 2.5 Flash model. `temperature=0.7` controls how creative/random the AI is allowed to be (0.0 means completely rigid and factual, 1.0 means highly creative). 0.7 is a good middle ground.
   *   **`chain = summary_prompt_template | llm`**: This illustrates the true power of Langchain! The `|` (pipe) symbol strings operations together sequentially. This line essentially says: "First, take the completely structured `summary_prompt_template`. Then, pass the resulting prompt directly into the Gemini `llm`." This combined workflow pipeline is known as a "chain".
   *   **`response = chain.invoke(input={"information": information})`**: This is the action step where network traffic happens. We tell the chain to `invoke` (run). We supply a dictionary `{"information": information}` telling it to grab our large multi-line biography and plug it securely into the `{information}` variable slot. Langchain then fires that complete request over the internet to Google's Gemini and awaits the answer.
   *   **`print(response.content)`**: The `response` that comes back from the AI contains various technical metadata. We only care about the actual text it typed back. `.content` extracts just the text portion, which we then print to the screen.

   *   **`if __name__ == "__main__": main()`**: This is standard Python boilerplate. It guarantees that the `main()` function is executed *only* if you run this script directly from the terminal, preventing it from accidentally running if you decide to import this file into another python script later.

8. Format your code using the tools you installed:
   ```powershell
   uv run isort .
   uv run black .
   ```
   **What this does (for beginners):**
   Because we installed `isort` and `black` inside our `uv` project environment (and not globally on your computer), your terminal won't recognize the `black` or `isort` commands directly. 
   By using `uv run`, you are telling `uv` to look inside your project's isolated environment, find `isort` and `black`, and run them on the current folder (which is what the `.` means). 
   - `isort .` will fix all the imports in all your project files.
   - `black .` will fix the overall formatting (spaces, quotes, line lengths) in all your project files.

9. Run your code using `uv`:
   ```powershell
   uv run main.py
   ```
   **What this does (for beginners):**
   If you try to run your script using a simple "Play" button in your editor (like VS Code's Code Runner) or by just typing `python main.py`, it will likely crash with a `ModuleNotFoundError` (for example, saying it can't find `langchain_core`). 
   This happens because that normal "Play" button uses the global Python installed on your computer, which doesn't know about all the packages you just installed inside this specific project's isolated `.venv` folder.
   
   Using `uv run main.py` is the correct way to execute your script. It tells `uv`: "Hey, load up my project's secret environment with all my downloaded packages, and *then* run `main.py` using that."

10. Expected Output from your script:
    When you successfully run `uv run main.py`, after a few moments waiting for the AI to respond, you should see output similar to this:

    ```text
    Hello from practice!
    [YOUR_SECRET_API_KEY_WILL_PRINT_HERE]
    Here's the summary and two interesting facts about Elon Musk based on the provided text:

    **1. Short Summary:**
    Elon Reeve Musk, born in South Africa in 1971, is a leading businessman and entrepreneur holding Canadian and American citizenship. He is primarily known for his leadership of Tesla (electric vehicles), SpaceX (space technology), X (formerly Twitter), and xAI (AI research), and for co-founding PayPal. Having been the world's wealthiest person since 2025, with an estimated net worth of $852 billion as of February 2026, Musk is also a highly polarizing public figure. He has drawn significant criticism for his political views, support of far-right causes, promotion of misinformation, and controversies surrounding hate speech on his social platform, X, and his brief role in the second Trump administration.

    **2. Two Interesting Facts:**
    *   In November 2025, a Tesla pay package worth an unprecedented $1 trillion for Musk was approved, which he is set to receive over 10 years if he meets specific company goals.
    *   After supporting Donald Trump in the 2024 election, Musk served as Senior Advisor to President Trump and the de facto head of the Department of Government Efficiency (DOGE) in early 2025, but later left the administration following a public feud with Trump.
    ```
