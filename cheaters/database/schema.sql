CREATE TABLE if not exists Students(
  Id INTEGER PRIMARY KEY AUTOINCREMENT,
  StudentNumber TEXT,
  CourseCode TEXT );

INSERT OR REPLACE INTO Students VALUES (1, 'hmdyas001', 'mam3000w');

 CREATE TABLE if not exists Assignments(
  Id INTEGER PRIMARY KEY AUTOINCREMENT,
  CourseCode TEXT,
  AssignmentDescription TEXT,
  DueDate DATE
 );

INSERT OR REPLACE INTO Assignments VALUES (1, 'CSC3002W', 'Capstone Project', date(2015, 1, 1));
INSERT OR REPLACE INTO Assignments VALUES (2, 'MAM3000W', 'Final math project', date(2016, 1, 1));

CREATE TABLE if not exists Submissions(
  Id INTEGER PRIMARY KEY AUTOINCREMENT,
  StudentId INTEGER NOT NULL,
  AssignmentNumber INT,
  ProgramSource TEXT,
  SubmissionDate DATE DEFAULT CURRENT_DATE,
  FOREIGN KEY (StudentId) REFERENCES Students(StudentNumber),
  FOREIGN KEY (AssignmentNumber) REFERENCES Assignments(Id)

);

 CREATE TABLE if not exists Signatures(
  Id INTEGER PRIMARY KEY AUTOINCREMENT,
  LineNumber INT,
  NgramHash INT,
  SubmissionId INT,
  FOREIGN KEY (SubmissionId) REFERENCES Submissions(Id)
 );

CREATE INDEX IF NOT EXISTS signature_submission ON Signatures (SubmissionId);


CREATE TABLE if not exists Matches(
  Id INTEGER PRIMARY KEY AUTOINCREMENT,
  SubmissionIdMine INT,
  StartLineMine INT,
  SubmissionIdTheirs INT,
  StartLineTheirs INT,
  LengthOfMatch INT,
  FOREIGN KEY (SubmissionIdMine) REFERENCES Submissions(Id),
  FOREIGN KEY (SubmissionIdTheirs) REFERENCES Submissions(Id)
);
