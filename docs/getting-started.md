# Getting Started

Welcome! This tutorial provides an introduction to the main features of Granite.Code. To complete it, we suggest that you have a running instance of VS Code with the Granite.Code extension enabled.

## Setup your workspace

For the best experience, we recommend moving the Granite.Code chat bar to the secondary sidebar, so that it is visible alongside the code editor. To do this:

* If the secondary side bar is not visible, show it by clicking the **Toggle Secondary Side Bar** button in the VS Code header.
* Find the Granite.Code icon in the Activity Bar, then drag it to the secondary side bar header.
* The Granite.Code side bar should now be located next to the VS Code editor area.

Once you have your workspace how you want it, we'll get started with Granite.Code's features.

## Ask questions

Granite.Code provides an interactive chat feature, which can be used to ask Granite models questions.

To use the chat, either click on the "Ask anything" prompt, or use the **Ctrl+L** keyboard shortcut. Then enter your question and press return.

The Granite code assistant can answer a range of question types, such as:

* TODO
* TODO
* TODO

Try some of these out now, to see what kind of responses you get.

Once you have asked a question, you can ask a follow-up question. For example, TODO.

## Ask about a code snippet

In addition to being able to ask general coding questions, you can also ask Granite questions about a snippet code or project. This can be useful for understanding how a piece of code works, or improving a small section of code.

To ask a question about a code snippet:

* In the editor, highlight the code you want to ask a question about
* Use the **Ctrl+L** keyboard shortcut to start a chat, or use the **Granite.Code > Add Highlighted Code to Context** context menu item
* The code snippet will be shown in the chat prompt, ready to be queried

You can try this using the code snippet below:

* Copy the snippet to a Python file
* Highlight the code to add it to the chat
* In the chat prompt, ask: "what sorting algorithm is this?"

```
def sorting_algorithm(x):
    for i in range(len(x)):
        for j in range(len(x) - 1):
            if x[j] > x[j + 1]:
                x[j], x[j + 1] = x[j + 1], x[j]
    return x
```

## Use Granite to make changes

Granite.Code also allows making code changes by giving instructions to the AI assistant. An easy way to try this is to edit a code snippet:

* In the editor, highlight the code you want to change
* Use the **Ctrl+E** keyboard shortcut to add the snippet to the prompt, and switch to edit mode
* Write how you want the code to be changed, then press return or click the **⏎ Enter** button

You can try this with the code snippet below:

* Copy the snippet to a Python file
* Highlight the code to add it to the chat
* In the chat, enter "make this more readable", and press return

```
def sorting_algorithm(x):
    for i in range(len(x)):
        for j in range(len(x) - 1):
            if x[j] > x[j + 1]:
                x[j], x[j + 1] = x[j + 1], x[j]
    return x
```

## Autocompletion

Granite.Code can make suggestions as you type. Suggestions are shown after the cursor. To accept a suggestion, just press **Tab**.

To try out autocomplete:

* Copy the snippet below into a Python file
* Place the cursor at the end of the line, then press **Enter**
* When the suggestion is shown, press **Tab**

```
# Basic assertion for sorting_algorithm...
```

## Next steps

This tutorial covers just a few of the basic Granite.Code features. Once you have mastered them, it is time to [learn how to get more from Granite.Code](FIXME).
