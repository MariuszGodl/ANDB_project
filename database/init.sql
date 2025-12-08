DROP TABLE IF EXISTS AuditLog;
DROP TABLE IF EXISTS SupportingDocument;
DROP TABLE IF EXISTS Application;
DROP TABLE IF EXISTS Student;

-- Student Table
CREATE TABLE Student (
    StudentID SERIAL PRIMARY KEY,
    FirstName VARCHAR(100) NOT NULL,
    LastName VARCHAR(100) NOT NULL,
    Email VARCHAR(255) NOT NULL UNIQUE CHECK (Email LIKE '%_@__%.__%'),
    PhoneNo VARCHAR(20),
    DateOfBirth DATE NOT NULL CHECK (DateOfBirth <= CURRENT_DATE),
    Address VARCHAR(255) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Application Table
CREATE TABLE Application (
    ApplicationID SERIAL PRIMARY KEY,
    StudentID INT NOT NULL,
    Status VARCHAR(50) NOT NULL DEFAULT 'Draft' CHECK (Status IN ('Draft', 'Submitted', 'Under Review', 'Accepted', 'Rejected')),
    AcademicYear INT NOT NULL,
    GPA DECIMAL(3, 2) NOT NULL CHECK (GPA >= 0.00 AND GPA <= 5.00),
    EssayText TEXT NOT NULL,
    ApplicationDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_student FOREIGN KEY (StudentID) REFERENCES Student(StudentID)
);

-- Supporting Document Table
CREATE TABLE SupportingDocument (
    DocumentID SERIAL PRIMARY KEY,
    ApplicationID INT NOT NULL,
    FileName VARCHAR(255) NOT NULL,
    FilePath VARCHAR(512) NOT NULL,
    FileType VARCHAR(50) NOT NULL,
    FileSizeKB INT NOT NULL CHECK (FileSizeKB > 0),
    UploadDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_application FOREIGN KEY (ApplicationID) REFERENCES Application(ApplicationID)
);

-- Audit Log Table
CREATE TABLE AuditLog (
    LogID SERIAL PRIMARY KEY,
    Timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    EventType VARCHAR(50) NOT NULL,
    Details TEXT
);

-- Indexes for performance optimization
CREATE INDEX idx_student_email ON Student(Email);
CREATE INDEX idx_application_status ON Application(Status);
CREATE INDEX idx_document_application ON SupportingDocument(ApplicationID);
CREATE INDEX idx_auditlog_eventtype ON AuditLog(EventType);