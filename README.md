
Advanced Library Management CLI project
Overview: Enhance the existing Library Management CLI Project by implementing a Lend Book feature that allows users to borrow books and updates the system accordingly.
Requirements: 
- Add a "Lend Book" option to the existing Library Management CLI menu.
- When someone borrows book, collect borrower's name, phone number, book title, and assign a return due date using datetime. Save them in a file.
- When someone lends a book, the quantity of the book will decrease.
- When the borrower returns the book, remove their lend info from the lend book file.
- When the borrower returns the book, the quantity of the book will increase.
- If there are no books available to lend, a message should be printed saying, "There are not enough books available to lend."
