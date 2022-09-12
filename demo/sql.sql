CREATE TABLE Vocabulary(  
    word CHAR(255) PRIMARY KEY,
    paraphrase VARCHAR(1023) NOT NULL,
    roots CHAR(255) NOT NULL,
    dates INT NOT NULL,
    counts INT NOT NULL
);