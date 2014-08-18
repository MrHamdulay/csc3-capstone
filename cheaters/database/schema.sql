CREATE TABLE if not exists Students(
  Id INT PRIMARY KEY,
  StudentNumber TEXT,
  CourseCode TEXT );

INSERT OR IGNORE INTO Students VALUES (1, 'hmdyas001', 'mam3000w');

 CREATE TABLE if not exists Assignments(
  Id INT PRIMARY KEY,
  CourseCode TEXT,
  AssignmentDescription TEXT,
  DueDate DATE
 );

CREATE TABLE if not exists Submissions(
  Id INT PRIMARY KEY,
  StudentId INT NOT NULL,
  AssignmentNumber INT,
  ProgramSource TEXT,
  SubmissionDate DATE DEFAULT CURRENT_DATE,
  FOREIGN KEY (StudentId) REFERENCES Students(ID),
  FOREIGN KEY (AssignmentNumber) REFERENCES Assignments(Id)

);

 CREATE TABLE if not exists Signatures(
  Id INT PRIMARY KEY,
  LineNumber INT,
  NgramHash INT,
  SubmissionId INT,
  FOREIGN KEY (SubmissionId) REFERENCES Submissions(Id)
 );


CREATE TABLE if not exists Matches(
  Id INT PRIMARY KEY,
  SubmissionId INT,
  LinesMatched INT,
  LengthOfMatch INT,
  FOREIGN KEY (SubmissionId) REFERENCES Submissions(Id));
