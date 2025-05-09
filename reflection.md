# Reflection

Student Name:  Kiritu Gachuki
Student Email:  kgachuki@syr.edu

## Instructions

Reflection is a key activity of learning. It helps you build a strong metacognition, or "understanding of your own learning." A good learner not only "knows what they know", but they "know what they don't know", too. Learning to reflect takes practice, but if your goal is to become a self-directed learner where you can teach yourself things, reflection is imperative.

- Now that you've completed the assignment, share your throughts. What did you learn? What confuses you? Where did you struggle? Where might you need more practice?
- A good reflection is: **specific as possible**,  **uses the terminology of the problem domain** (what was learned in class / through readings), and **is actionable** (you can pursue next steps, or be aided in the pursuit). That last part is what will make you a self-directed learner.
- Flex your recall muscles. You might have to review class notes / assigned readings to write your reflection and get the terminology correct.
- Your reflection is for **you**. Yes I make you write them and I read them, but you are merely practicing to become a better self-directed learner. If you read your reflection 1 week later, does what you wrote advance your learning?

Examples:

- **Poor Reflection:**  "I don't understand loops."   
**Better Reflection:** "I don't undersand how the while loop exits."   
**Best Reflection:** "I struggle writing the proper exit conditions on a while loop." It's actionable: You can practice this, google it, ask Chat GPT to explain it, etc. 
-  **Poor Reflection** "I learned loops."   
**Better Reflection** "I learned how to write while loops and their difference from for loops."   
**Best Reflection** "I learned when to use while vs for loops. While loops are for sentiel-controlled values (waiting for a condition to occur), vs for loops are for iterating over collections of fixed values."

`--- Reflection Below This Line ---`
In this project, I developed by own ETL pipeline exploring data related to the Sudanese Civil War.
Although I understood the overall structure I needed for this project, there were a few issues I encountered
trying to implement them. The first was extracting the data from the APIs. The ACLED data went smoothly since I
had used it before but with R. The HDX data was the most challenging, as I tried to use their custom API that relies on
special classes and functions to retrieve the data. It took a while to understand how their "datasets" work, even with their
examples, but I figured out how to find the data I needed through their documentation. The cleaning and preparation was not too
difficult, just a lot of fixing small formatting errors as they showed up. One example was the excel column names having
whitespace around them, which I addressed by using strip on the column names. The dashboard was the longest script, but it
was suprisingly straightforward once I knew what data I wanted to show. Getting the toggles to work properly was the hardest
part, but I realized I needed to check if the toggle was on AND the selection was made to not get errors when filtering the map.