SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[EmployeeMaster_Payroll](
	[ID] [nvarchar](255) NULL,
	[Circle] [nvarchar](255) NULL,
	[EmployeeID] [float] NULL,
	[EmployeeName] [nvarchar](255) NULL,
	[DateOfBirth] [datetime] NULL,
	[Age] [nvarchar](255) NULL,
	[DateOfJoining] [datetime] NULL,
	[Department] [nvarchar](255) NULL,
	[Designation] [nvarchar](255) NULL,
	[Salary] [nvarchar](255) NULL,
	[BankAccountNum] [float] NULL,
	[BankName] [nvarchar](255) NULL,
	[BankCode] [nvarchar](255) NULL,
	[PANNumber] [nvarchar](255) NULL,
	[Address] [nvarchar](255) NULL,
	[Location] [nvarchar](255) NULL,
	[ContactNumber] [float] NULL,
	[EmploymentStatus] [nvarchar](255) NULL,
	[DateOfLeaving] [nvarchar](255) NULL,
	[OtherAllowances1] [float] NULL,
	[OtherAllowances2] [float] NULL,
	[OtherAllowances3] [float] NULL,
	[OtherAllowances4] [float] NULL,
	[OtherAllowances5] [float] NULL,
	[Conveyance] [float] NULL,
	[BasicSalary] [float] NULL,
	[HRA] [float] NULL,
	[DA] [nvarchar](255) NULL,
	[Bonus] [nvarchar](255) NULL,
	[TotalCTC] [float] NULL,
	[CreationDate] [datetime] NULL,
	[CreatedDate] [datetime] NULL,
	[CreatedBy] [nvarchar](255) NULL,
	[UpdatedDate] [nvarchar](255) NULL,
	[UpdatedBy] [nvarchar](255) NULL,
	[ModifiedBy] [nvarchar](255) NULL,
	[ModifiedDate] [datetime] NULL,
	[ExeVersionNo] [nvarchar](255) NULL,
	[ModuleName] [nvarchar](255) NULL,
	[EnteredOnMachineID] [nvarchar](255) NULL,
	[ClientCode] [float] NULL,
	[SessionID] [nvarchar](255) NULL,
	[Grade] [nvarchar](255) NULL
) ON [PRIMARY]
GO
/****** Object:  View [dbo].[P2p1]    Script Date: 7/29/2020 7:11:09 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
 --44 Duplicate Employees in Employee Master by PAN
create view [dbo].[P2p1] as
(
 SELECT distinct BT.EmployeeID, BT.EmployeeName, BT.DateOfBirth, BT.Age, BT.DateOfJoining, BT.Department, BT.Designation, BT.Salary, BT.BankAccountNum, BT.BankName, BT.BankCode, BT.PANNumber, 
BT.Address, BT.Location, BT.ContactNumber, BT.EmploymentStatus, BT.DateOfLeaving, BT.OtherAllowances1, BT.OtherAllowances2, BT.OtherAllowances3, BT.OtherAllowances4, BT.OtherAllowances5, 
BT.Conveyance, BT.BasicSalary, BT.HRA, BT.DA, BT.Bonus, BT.TotalCTC, BT.Grade,BT.SessionID
FROM  ( select PANNumber ,count(PANNumber) as AggregateResult from EmployeeMaster_Payroll as T1  where  PANNumber is not null and PANNumber<>'' Group By PANNumber    having  count(PANNumber) >1) AS RT INNER JOIN EmployeeMaster_Payroll AS BT ON BT.PANNumber = RT.PANNumber 
)
GO
/****** Object:  View [dbo].[P2p2]    Script Date: 7/29/2020 7:11:09 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
--54 Duplicate Employees in Employee Master by Bank Account No.

create view [dbo].[P2p2] as
(
  SELECT distinct  BT.EmployeeID, BT.EmployeeName, BT.DateOfBirth, BT.Age, BT.DateOfJoining, BT.Department,
   BT.Designation, BT.Salary, BT.BankAccountNum, BT.BankName, BT.BankCode, BT.PANNumber, 
BT.Address, BT.Location, BT.ContactNumber, BT.EmploymentStatus, BT.DateOfLeaving, BT.OtherAllowances1, BT.OtherAllowances2,
 BT.OtherAllowances3, BT.OtherAllowances4, BT.OtherAllowances5, 
BT.Conveyance, BT.BasicSalary, BT.HRA, BT.DA, BT.Bonus, BT.TotalCTC, BT.Grade,bt.SessionID
FROM ( select BankAccountNum ,count(BankAccountNum) as AggregateResult from EmployeeMaster_Payroll as T1    Group By SessionID,BankAccountNum,ClientCode    having  count(BankAccountNum) >1) AS RT INNER JOIN EmployeeMaster_Payroll AS BT ON BT.BankAccountNum = RT.BankAccountNum  
)
GO
/****** Object:  Table [dbo].[PayrollFile_Payroll]    Script Date: 7/29/2020 7:11:09 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[PayrollFile_Payroll](
	[ID] [nvarchar](255) NULL,
	[Circle] [nvarchar](255) NULL,
	[EmployeeID] [float] NULL,
	[Grade] [nvarchar](255) NULL,
	[Designation] [nvarchar](255) NULL,
	[JoiningDate] [datetime] NULL,
	[MonthofPayroll] [datetime] NULL,
	[NoOfDays] [float] NULL,
	[LWP] [nvarchar](255) NULL,
	[BasicSalary] [float] NULL,
	[BasicSalaryArrears] [float] NULL,
	[HRA] [float] NULL,
	[HRAArrears] [float] NULL,
	[DA] [float] NULL,
	[DAArrears] [float] NULL,
	[Conveyance] [float] NULL,
	[ConveyanceArrears] [float] NULL,
	[Overtime] [nvarchar](255) NULL,
	[OvertimeArrears] [nvarchar](255) NULL,
	[OtherAllowances1] [float] NULL,
	[OtherAllowancesArrears1] [float] NULL,
	[OtherAllowances2] [float] NULL,
	[OtherAllowances3] [float] NULL,
	[OtherAllowances4] [float] NULL,
	[OtherAllowances5] [nvarchar](255) NULL,
	[Bonus] [float] NULL,
	[GrossSalary] [float] NULL,
	[PFDeduction] [float] NULL,
	[PTDeduction] [float] NULL,
	[ESI] [float] NULL,
	[IncomeTax] [nvarchar](255) NULL,
	[OtherDeduction] [float] NULL,
	[GrossDeductions] [float] NULL,
	[NetSalary] [float] NULL,
	[ModeOfPayment] [nvarchar](255) NULL,
	[BankName] [nvarchar](255) NULL,
	[BankAccNo] [float] NULL,
	[CreatedBy] [nvarchar](255) NULL,
	[CreatedDate] [datetime] NULL,
	[ModifiedBy] [nvarchar](255) NULL,
	[ModifiedDate] [datetime] NULL,
	[ExeVersionNo] [nvarchar](255) NULL,
	[ModuleName] [nvarchar](255) NULL,
	[EnteredOnMachineID] [nvarchar](255) NULL,
	[ClientCode] [float] NULL,
	[SessionID] [nvarchar](255) NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[TerminatedEmployeeListing_Payroll]    Script Date: 7/29/2020 7:11:09 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[TerminatedEmployeeListing_Payroll](
	[ID] [nvarchar](255) NULL,
	[Circle] [nvarchar](255) NULL,
	[EmployeeID] [float] NULL,
	[EmployeeName] [nvarchar](255) NULL,
	[Grade] [nvarchar](255) NULL,
	[TypeOfSeparation] [nvarchar](255) NULL,
	[DateOfResignation] [datetime] NULL,
	[DateOfRelease] [datetime] NULL,
	[NoticePeriod] [float] NULL,
	[ReasonForSeparation] [nvarchar](255) NULL,
	[CreatedBy] [nvarchar](255) NULL,
	[CreatedDate] [datetime] NULL,
	[ModifiedBy] [nvarchar](255) NULL,
	[ModifiedDate] [datetime] NULL,
	[ExeVersionNo] [nvarchar](255) NULL,
	[ModuleName] [nvarchar](255) NULL,
	[EnteredOnMachineID] [nvarchar](255) NULL,
	[ClientCode] [float] NULL,
	[SessionID] [nvarchar](255) NULL
) ON [PRIMARY]
GO
/****** Object:  View [dbo].[P2p4]    Script Date: 7/29/2020 7:11:09 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
--327  Payments to employees after the employee leave date

create view [dbo].[P2p4] as
(
 SELECT distinct lt.DateOfRelease AS 'DateOfRelease as per Terminated Employee Listing', BT.MonthofPayroll, BT.Circle, BT.Grade, BT.Designation, BT.JoiningDate,  BT.NoOfDays, BT.LWP, BT.NetSalary, BT.EmployeeID,lt.SessionID FROM  PayrollFile_Payroll AS BT INNER JOIN
TerminatedEmployeeListing_Payroll AS lt ON lt.EmployeeID = BT.EmployeeID 
 where  month(MonthofPayroll)>=month(DateOfRelease)
 )
GO
/****** Object:  View [dbo].[P2p3]    Script Date: 7/29/2020 7:11:09 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

create view [dbo].[P2p3] as
(
--320  Payments made to more than one bank account of the same Employee across various months
SELECT distinct BT.EmployeeID,BT.BankAccNo, BT.JoiningDate, BT.MonthofPayroll,bt.NetSalary,
 BT.NoOfDays,BT.ModeOfPayment, BT.BankName,bt.sessionid from PayrollFile_Payroll bt inner join(
select  CleanData  from (select ltrim(rtrim(EmployeeID)) cleandata ,V.BankAccNo from PayrollFile_Payroll v 
 group by ltrim(rtrim(EmployeeID)),V.BankAccNo ) as AA group by cleandata  having count(cleandata)> 1) t2 on
 ltrim(rtrim(EmployeeID))=cleandata
 )
GO
/****** Object:  Table [dbo].[Payments_Data_SCM]    Script Date: 7/29/2020 7:11:09 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Payments_Data_SCM](
	[ID] [nvarchar](255) NULL,
	[Payment_Number] [float] NULL,
	[Invoice_Number] [nvarchar](255) NULL,
	[Invoice_Date] [datetime] NULL,
	[Invoice_Amount] [float] NULL,
	[Amount_Paid] [float] NULL,
	[Currency] [nvarchar](255) NULL,
	[GL_Account_Number] [nvarchar](255) NULL,
	[Check_Wire] [nvarchar](255) NULL,
	[Created_By] [nvarchar](255) NULL,
	[Bill_Date] [nvarchar](255) NULL,
	[Receipt_Date] [nvarchar](255) NULL,
	[Vendor_Invoice_Number] [nvarchar](255) NULL,
	[Vendor_Invoice_Date] [datetime] NULL,
	[Invoice_Pressing_Number] [nvarchar](255) NULL,
	[Payment_Date] [datetime] NULL,
	[Vendor_Number] [float] NULL,
	[Vendor_Name] [nvarchar](255) NULL,
	[PO_Number] [nvarchar](255) NULL,
	[PO_Date] [nvarchar](255) NULL,
	[Invoice_Receipt_Date] [nvarchar](255) NULL,
	[Credit_Terms] [nvarchar](255) NULL,
	[Payment_Due_Date] [datetime] NULL,
	[Bank_Account_Number] [nvarchar](255) NULL,
	[Vendor_Bank_Name] [nvarchar](255) NULL,
	[Vendor_Bank_Code] [nvarchar](255) NULL,
	[Vendor_Location] [nvarchar](255) NULL,
	[Vendor_PAN_Number] [nvarchar](255) NULL,
	[User_ID] [nvarchar](255) NULL,
	[Mode_Of_Payment] [nvarchar](255) NULL,
	[Material_Code] [nvarchar](255) NULL,
	[Material_Description] [nvarchar](255) NULL,
	[Quantity] [nvarchar](255) NULL,
	[SessionID] [nvarchar](255) NULL,
	[AuditFrom] [nvarchar](255) NULL,
	[AuditTo] [nvarchar](255) NULL,
	[ClientCode] [float] NULL,
	[EngagementCode] [nvarchar](255) NULL,
	[CreatedBy] [nvarchar](255) NULL,
	[CreatedDate] [datetime] NULL,
	[ModifiedBy] [nvarchar](255) NULL,
	[ModifiedDate] [datetime] NULL,
	[ExeVersionNo] [nvarchar](255) NULL,
	[ModuleName] [nvarchar](255) NULL,
	[EnteredOnMachineID] [nvarchar](255) NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Vendor_master_SCM]    Script Date: 7/29/2020 7:11:09 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Vendor_master_SCM](
	[ID] [nvarchar](255) NULL,
	[Vendor_Number] [float] NULL,
	[Vendor_Name] [nvarchar](255) NULL,
	[Bank_Account_Number] [nvarchar](255) NULL,
	[Bank_Name] [nvarchar](255) NULL,
	[Region] [nvarchar](255) NULL,
	[Bank_Code] [nvarchar](255) NULL,
	[PAN_Number] [nvarchar](255) NULL,
	[Location] [nvarchar](255) NULL,
	[Currency] [nvarchar](255) NULL,
	[P_Org] [nvarchar](255) NULL,
	[Plant] [nvarchar](255) NULL,
	[Vendor_Type] [nvarchar](255) NULL,
	[Partner_Function] [nvarchar](255) NULL,
	[Group_Source] [nvarchar](255) NULL,
	[Bill_Payment_Block] [nvarchar](255) NULL,
	[Vendor_Tax_Code] [nvarchar](255) NULL,
	[Inco_Terms] [nvarchar](255) NULL,
	[Payment_Method] [nvarchar](255) NULL,
	[Tax_Code] [nvarchar](255) NULL,
	[Address_1] [nvarchar](255) NULL,
	[Address_2] [nvarchar](255) NULL,
	[Address_3] [nvarchar](255) NULL,
	[Address_4] [nvarchar](255) NULL,
	[Address_5] [nvarchar](255) NULL,
	[Address_6] [nvarchar](255) NULL,
	[Contact_Number_2] [nvarchar](255) NULL,
	[Contact_Number_3] [nvarchar](255) NULL,
	[One_Time_Vendor] [nvarchar](255) NULL,
	[Payment_Terms] [nvarchar](255) NULL,
	[Tax_ID] [nvarchar](255) NULL,
	[Status] [nvarchar](255) NULL,
	[Creation_Date] [datetime] NULL,
	[Created_By] [nvarchar](255) NULL,
	[Last_Update_date] [datetime] NULL,
	[GSTN] [nvarchar](255) NULL,
	[Last_update_By] [nvarchar](255) NULL,
	[SessionID] [nvarchar](255) NULL,
	[AuditFrom] [nvarchar](255) NULL,
	[AuditTo] [nvarchar](255) NULL,
	[ClientCode] [nvarchar](255) NULL,
	[EngagementCode] [nvarchar](255) NULL,
	[CreatedBy] [nvarchar](255) NULL,
	[CreatedDate] [datetime] NULL,
	[ModifiedBy] [nvarchar](255) NULL,
	[ModifiedDate] [datetime] NULL,
	[ExeVersionNo] [nvarchar](255) NULL,
	[ModuleName] [nvarchar](255) NULL,
	[EnteredOnMachineID] [nvarchar](255) NULL,
	[Contact_Number_1] [float] NULL
) ON [PRIMARY]
GO
/****** Object:  View [dbo].[AP1]    Script Date: 7/29/2020 7:11:09 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

 create view [dbo].[AP1] as 
 Select distinct bt.Vendor_Number as [VendorNumber], bt.Vendor_Name as [VendorName], bt.Status, bt.Bill_Payment_Block as [Bill/Payment Block],
 lt.Payment_Number as [PaymentNumber], lt.Payment_Date as [PaymentDate], lt.Amount_Paid as [AmountPaid], '' as [Cheque/Wire],
 bt.PAN_Number as [PANNumber], bt.Currency, bt.Payment_Terms,bt.SessionID
from Vendor_Master_SCM as bt inner join Payments_Data_SCM as lt on bt.Vendor_Number = lt.Vendor_Number
where bt.Status = 'Inactive' AND bt.Bill_Payment_Block = 'Y'
GO
/****** Object:  View [dbo].[AP2]    Script Date: 7/29/2020 7:11:09 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
 create view [dbo].[AP2] as 
select BT.Payment_Number, BT.Invoice_Number, BT.Invoice_Date, BT.Invoice_Amount, BT.Amount_Paid,BT.Payment_Date, BT.Payment_Due_Date,
datediff(day, bt.Payment_Due_Date, bt.Payment_Date) as [EarlyPaymentOrDelayPayment], bt.Currency, bt.GL_Account_Number as [G/LAccountNumber],
'' as [Cheque/Wire], bt.created_by as [CreatedBy], bt.Bill_Date, bt.Receipt_Date as [ReceiptDate], bt.Vendor_Invoice_Number as [VendorInvoiceNumber],bt.Invoice_Pressing_Number as [InvoiceProcessingNumber], bt.Vendor_Number, bt.Vendor_Name, bt.PO_Number,
bt.PO_Date, bt.Invoice_Receipt_Date, bt.Credit_Terms, bt.Bank_Account_Number, bt.Vendor_Bank_Name, bt.Vendor_Bank_Code, bt.Vendor_Location, bt.Vendor_PAN_Number, bt.User_ID, bt.Mode_Of_Payment, bt.Material_Code, bt.Material_Description, bt.Quantity
 from Payments_Data_SCM as bt where datediff(day, Payment_Due_Date,Payment_Date)>0
GO
/****** Object:  View [dbo].[INTERNAL_TABLE_CNT]    Script Date: 7/29/2020 7:11:09 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE VIEW [dbo].[INTERNAL_TABLE_CNT]
AS
SELECT T.NAME COLLATE Latin1_General_CI_AI as 'T_name', P.[ROWS] as 'counts'
 FROM SYS.TABLES T INNER JOIN SYS.PARTITIONS P ON T.OBJECT_ID=P.OBJECT_ID
GO
/****** Object:  Table [dbo].[ChangeList]    Script Date: 7/29/2020 7:11:09 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[ChangeList](
	[ChangeList] [nchar](10) NULL,
	[ID] [varchar](50) NULL,
	[SessionID] [varchar](50) NULL,
	[AuditFrom] [date] NULL,
	[AuditTo] [date] NULL,
	[ClientCode] [varchar](50) NULL,
	[EngagementCode] [varchar](50) NULL,
	[CreatedBy] [varchar](250) NULL,
	[CreatedDate] [date] NULL,
	[ModifiedBy] [varchar](255) NULL,
	[ModifiedDate] [datetime] NULL,
	[ExeVersionNo] [varchar](255) NULL,
	[ModuleName] [varchar](255) NULL,
	[EnteredOnMachineID] [varchar](255) NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[ChangeMgmt]    Script Date: 7/29/2020 7:11:09 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[ChangeMgmt](
	[fadsf] [nchar](10) NULL,
	[ID] [varchar](50) NULL,
	[SessionID] [varchar](50) NULL,
	[AuditFrom] [date] NULL,
	[AuditTo] [date] NULL,
	[ClientCode] [varchar](50) NULL,
	[EngagementCode] [varchar](50) NULL,
	[CreatedBy] [varchar](250) NULL,
	[CreatedDate] [date] NULL,
	[ModifiedBy] [varchar](255) NULL,
	[ModifiedDate] [datetime] NULL,
	[ExeVersionNo] [varchar](255) NULL,
	[ModuleName] [varchar](255) NULL,
	[EnteredOnMachineID] [varchar](255) NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[ChangeMgmt_List]    Script Date: 7/29/2020 7:11:09 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[ChangeMgmt_List](
	[mfund_deal_id] [nvarchar](255) NULL,
	[deal_id] [nvarchar](255) NULL,
	[Exchange/ OTC] [nvarchar](255) NULL,
	[Type] [nvarchar](255) NULL,
	[broker] [nvarchar](255) NULL,
	[Trader] [nvarchar](255) NULL,
	[Trade reviewer] [nvarchar](255) NULL,
	[Trade Date] [datetime] NULL,
	[Allcation Date] [datetime] NULL,
	[Fund Name] [nvarchar](255) NULL,
	[Security Code] [nvarchar](255) NULL,
	[Type of security] [nvarchar](255) NULL,
	[Sector] [nvarchar](255) NULL,
	[PM] [nvarchar](255) NULL,
	[tran_type] [nvarchar](255) NULL,
	[quantity] [float] NULL,
	[price] [float] NULL,
	[brk_commn] [float] NULL,
	[Total Value] [float] NULL,
	[Country] [nvarchar](255) NULL,
	[account] [nvarchar](255) NULL,
	[Error type] [nvarchar](255) NULL,
	[Breach type description] [nvarchar](255) NULL,
	[Breach type] [nvarchar](255) NULL,
	[Breach Reason] [nvarchar](255) NULL,
	[ID] [varchar](50) NULL,
	[SessionID] [varchar](50) NULL,
	[AuditFrom] [date] NULL,
	[AuditTo] [date] NULL,
	[ClientCode] [varchar](50) NULL,
	[EngagementCode] [varchar](50) NULL,
	[CreatedBy] [varchar](250) NULL,
	[CreatedDate] [date] NULL,
	[ModifiedBy] [varchar](255) NULL,
	[ModifiedDate] [datetime] NULL,
	[ExeVersionNo] [varchar](255) NULL,
	[ModuleName] [varchar](255) NULL,
	[EnteredOnMachineID] [varchar](255) NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[DBA_USERS]    Script Date: 7/29/2020 7:11:09 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[DBA_USERS](
	[Database] [nvarchar](255) NULL,
	[USERNAME] [nvarchar](255) NULL,
	[USER_ID] [nvarchar](255) NULL,
	[PASSWORD] [nvarchar](255) NULL,
	[ACCOUNT_STATUS] [nvarchar](255) NULL,
	[LOCK_DATE] [nvarchar](255) NULL,
	[EXPIRY_DA] [nvarchar](255) NULL,
	[DEFAULT_TABLESPACE] [nvarchar](255) NULL,
	[TEMPORARY_TABLESPACE] [nvarchar](255) NULL,
	[CREATED] [nvarchar](255) NULL,
	[PROFILE] [nvarchar](255) NULL,
	[INITIAL_RSRC_CONSUMER_GROUP] [nvarchar](255) NULL,
	[EXTERNAL_NAME] [nvarchar](255) NULL,
	[PASSWORD.1] [nvarchar](255) NULL,
	[E] [nvarchar](255) NULL,
	[AUTHENTI] [nvarchar](255) NULL,
	[SessionID] [varchar](50) NULL,
	[ID] [varchar](50) NULL,
	[ClientID] [varchar](50) NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[ExceptionsBroker]    Script Date: 7/29/2020 7:11:09 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[ExceptionsBroker](
	[mfund_deal_id] [nvarchar](255) NULL,
	[deal_id] [nvarchar](255) NULL,
	[Exchange/ OTC] [nvarchar](255) NULL,
	[Type] [nvarchar](255) NULL,
	[broker] [nvarchar](255) NULL,
	[Trader] [nvarchar](255) NULL,
	[Trade reviewer] [nvarchar](255) NULL,
	[Trade Date] [datetime] NULL,
	[Allcation Date] [datetime] NULL,
	[Fund Name] [nvarchar](255) NULL,
	[Security Code] [nvarchar](255) NULL,
	[Type of security] [nvarchar](255) NULL,
	[Sector] [nvarchar](255) NULL,
	[PM] [nvarchar](255) NULL,
	[tran_type] [nvarchar](255) NULL,
	[quantity] [float] NULL,
	[price] [float] NULL,
	[brk_commn] [float] NULL,
	[Total Value] [float] NULL,
	[account] [nvarchar](255) NULL,
	[ID] [varchar](50) NULL,
	[SessionID] [varchar](50) NULL,
	[AuditFrom] [date] NULL,
	[AuditTo] [date] NULL,
	[ClientCode] [varchar](50) NULL,
	[EngagementCode] [varchar](50) NULL,
	[CreatedBy] [varchar](250) NULL,
	[CreatedDate] [date] NULL,
	[ModifiedBy] [varchar](255) NULL,
	[ModifiedDate] [datetime] NULL,
	[ExeVersionNo] [varchar](255) NULL,
	[ModuleName] [varchar](255) NULL,
	[EnteredOnMachineID] [varchar](255) NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[ExceptionsTraderApprover]    Script Date: 7/29/2020 7:11:09 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[ExceptionsTraderApprover](
	[mfund_deal_id] [nvarchar](255) NULL,
	[deal_id] [nvarchar](255) NULL,
	[Exchange/ OTC] [nvarchar](255) NULL,
	[Type] [nvarchar](255) NULL,
	[broker] [nvarchar](255) NULL,
	[Trader] [nvarchar](255) NULL,
	[Trade reviewer] [nvarchar](255) NULL,
	[Trade Date] [datetime] NULL,
	[Allcation Date] [datetime] NULL,
	[Fund Name] [nvarchar](255) NULL,
	[Security Code] [nvarchar](255) NULL,
	[Type of security] [nvarchar](255) NULL,
	[Sector] [nvarchar](255) NULL,
	[PM] [nvarchar](255) NULL,
	[tran_type] [nvarchar](255) NULL,
	[quantity] [float] NULL,
	[price] [float] NULL,
	[brk_commn] [float] NULL,
	[Total Value] [float] NULL,
	[account] [nvarchar](255) NULL,
	[ID] [varchar](50) NULL,
	[SessionID] [varchar](50) NULL,
	[AuditFrom] [date] NULL,
	[AuditTo] [date] NULL,
	[ClientCode] [varchar](50) NULL,
	[EngagementCode] [varchar](50) NULL,
	[CreatedBy] [varchar](250) NULL,
	[CreatedDate] [date] NULL,
	[ModifiedBy] [varchar](255) NULL,
	[ModifiedDate] [datetime] NULL,
	[ExeVersionNo] [varchar](255) NULL,
	[ModuleName] [varchar](255) NULL,
	[EnteredOnMachineID] [varchar](255) NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[ExceptionsVacations]    Script Date: 7/29/2020 7:11:09 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[ExceptionsVacations](
	[mfund_deal_id] [nvarchar](255) NULL,
	[deal_id] [nvarchar](255) NULL,
	[Exchange/ OTC] [nvarchar](255) NULL,
	[Type] [nvarchar](255) NULL,
	[broker] [nvarchar](255) NULL,
	[Trader] [nvarchar](255) NULL,
	[Trade reviewer] [nvarchar](255) NULL,
	[Trade Date] [datetime] NULL,
	[Allcation Date] [datetime] NULL,
	[Fund Name] [nvarchar](255) NULL,
	[Security Code] [nvarchar](255) NULL,
	[Type of security] [nvarchar](255) NULL,
	[Sector] [nvarchar](255) NULL,
	[PM] [nvarchar](255) NULL,
	[tran_type] [nvarchar](255) NULL,
	[quantity] [float] NULL,
	[price] [float] NULL,
	[brk_commn] [float] NULL,
	[Total Value] [float] NULL,
	[account] [nvarchar](255) NULL,
	[ID] [varchar](50) NULL,
	[SessionID] [varchar](50) NULL,
	[AuditFrom] [date] NULL,
	[AuditTo] [date] NULL,
	[ClientCode] [varchar](50) NULL,
	[EngagementCode] [varchar](50) NULL,
	[CreatedBy] [varchar](250) NULL,
	[CreatedDate] [date] NULL,
	[ModifiedBy] [varchar](255) NULL,
	[ModifiedDate] [datetime] NULL,
	[ExeVersionNo] [varchar](255) NULL,
	[ModuleName] [varchar](255) NULL,
	[EnteredOnMachineID] [varchar](255) NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[InvestRules]    Script Date: 7/29/2020 7:11:09 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[InvestRules](
	[InvestRules] [nchar](10) NULL,
	[ID] [varchar](50) NULL,
	[SessionID] [varchar](50) NULL,
	[AuditFrom] [date] NULL,
	[AuditTo] [date] NULL,
	[ClientCode] [varchar](50) NULL,
	[EngagementCode] [varchar](50) NULL,
	[CreatedBy] [varchar](250) NULL,
	[CreatedDate] [date] NULL,
	[ModifiedBy] [varchar](255) NULL,
	[ModifiedDate] [datetime] NULL,
	[ExeVersionNo] [varchar](255) NULL,
	[ModuleName] [varchar](255) NULL,
	[EnteredOnMachineID] [varchar](255) NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Oracle_py_Output_attri_A]    Script Date: 7/29/2020 7:11:09 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Oracle_py_Output_attri_A](
	[Database] [nvarchar](255) NULL,
	[NUM] [nvarchar](255) NULL,
	[NAME] [nvarchar](255) NULL,
	[TYPE] [nvarchar](255) NULL,
	[VALUE] [nvarchar](255) NULL,
	[DISPLAY_VALUE] [nvarchar](255) NULL,
	[ISDEFA] [nvarchar](255) NULL,
	[ISSES] [nvarchar](255) NULL,
	[ISSYS_MOD] [nvarchar](255) NULL,
	[ISINS] [nvarchar](255) NULL,
	[ISMODIFIED] [nvarchar](255) NULL,
	[ISADJ] [nvarchar](255) NULL,
	[ISDEP] [nvarchar](255) NULL,
	[ISBAS] [nvarchar](255) NULL,
	[DESCRIPTION] [nvarchar](255) NULL,
	[ORDINAL] [nvarchar](255) NULL,
	[UPDATE_COMMENT] [nvarchar](255) NULL,
	[ExceptionFlag] [nvarchar](255) NULL,
	[SessionID] [varchar](50) NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Oracle_py_Output_attri_B]    Script Date: 7/29/2020 7:11:09 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Oracle_py_Output_attri_B](
	[Database] [nvarchar](255) NULL,
	[USERNAME] [nvarchar](255) NULL,
	[USER_ID] [nvarchar](255) NULL,
	[PASSWORD] [nvarchar](255) NULL,
	[ACCOUNT_STATUS] [nvarchar](255) NULL,
	[LOCK_DATE] [nvarchar](255) NULL,
	[EXPIRY_DA] [nvarchar](255) NULL,
	[DEFAULT_TABLESPACE] [nvarchar](255) NULL,
	[TEMPORARY_TABLESPACE] [nvarchar](255) NULL,
	[CREATED] [nvarchar](255) NULL,
	[PROFILE] [nvarchar](255) NULL,
	[INITIAL_RSRC_CONSUMER_GROUP] [nvarchar](255) NULL,
	[EXTERNAL_NAME] [nvarchar](255) NULL,
	[PASSWORD.1] [nvarchar](255) NULL,
	[E] [nvarchar](255) NULL,
	[AUTHENTI] [nvarchar](255) NULL,
	[ExceptionFlag] [nvarchar](255) NULL,
	[SessionID] [varchar](50) NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Sheet2$]    Script Date: 7/29/2020 7:11:09 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Sheet2$](
	[BU] [nvarchar](255) NULL,
	[BU Description] [nvarchar](255) NULL,
	[Employee ID] [nvarchar](255) NULL,
	[Employee] [nvarchar](255) NULL,
	[Report Name] [nvarchar](255) NULL,
	[Report ID] [nvarchar](255) NULL,
	[Policy] [nvarchar](255) NULL,
	[Org Unit 2 - Code] [nvarchar](255) NULL,
	[Org Unit 2 - Name] [nvarchar](255) NULL,
	[Approval Status] [nvarchar](255) NULL,
	[Transaction Type] [nvarchar](255) NULL,
	[Expense Type] [nvarchar](255) NULL,
	[Parent Expense Type] [nvarchar](255) NULL,
	[Ticket Number] [nvarchar](255) NULL,
	[Transaction Date] [nvarchar](255) NULL,
	[Sent for Payment Date] [nvarchar](255) NULL,
	[Personal] [nvarchar](255) NULL,
	[Payment Type] [nvarchar](255) NULL,
	[Reimbursement Currency] [nvarchar](255) NULL,
	[Expense Amount (reimbursement currency)] [nvarchar](255) NULL,
	[Transaction Currency] [nvarchar](255) NULL,
	[Expense Amount (transaction currency)] [nvarchar](255) NULL,
	[Reporting Currency] [nvarchar](255) NULL,
	[Expense Amount (rpt)] [nvarchar](255) NULL,
	[Approved Amount] [nvarchar](255) NULL,
	[Approved Amount (rpt)] [nvarchar](255) NULL,
	[Total Tax Posted Amount (rpt)] [nvarchar](255) NULL,
	[Total Tax Adjusted Amount (rpt)] [nvarchar](255) NULL,
	[Vendor] [nvarchar](255) NULL,
	[City/Location] [nvarchar](255) NULL,
	[Country] [nvarchar](255) NULL,
	[First Approved Date] [nvarchar](255) NULL,
	[First Submitted Date] [nvarchar](255) NULL,
	[Entry Key] [nvarchar](255) NULL,
	[Parent Entry Key] [nvarchar](255) NULL,
	[Distance Unit] [nvarchar](255) NULL,
	[Business Distance] [nvarchar](255) NULL,
	[Comment] [nvarchar](255) NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[TradeDump]    Script Date: 7/29/2020 7:11:09 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[TradeDump](
	[mfund_deal_id] [nvarchar](255) NULL,
	[deal_id] [nvarchar](255) NULL,
	[Exchange/ OTC] [nvarchar](255) NULL,
	[Type] [nvarchar](255) NULL,
	[broker] [nvarchar](255) NULL,
	[Trader] [nvarchar](255) NULL,
	[Trade reviewer] [nvarchar](255) NULL,
	[Trade Date] [datetime] NULL,
	[Allcation Date] [datetime] NULL,
	[Fund Name] [nvarchar](255) NULL,
	[Security Code] [nvarchar](255) NULL,
	[Type of security] [nvarchar](255) NULL,
	[Sector] [nvarchar](255) NULL,
	[PM] [nvarchar](255) NULL,
	[tran_type] [nvarchar](255) NULL,
	[quantity] [float] NULL,
	[price] [float] NULL,
	[brk_commn] [float] NULL,
	[Total Value] [float] NULL,
	[account] [nvarchar](255) NULL,
	[Error type] [nvarchar](255) NULL,
	[Approval taken] [nvarchar](255) NULL,
	[Breach type] [nvarchar](255) NULL,
	[Breach Reason] [nvarchar](255) NULL,
	[ID] [varchar](50) NULL,
	[SessionID] [varchar](50) NULL,
	[AuditFrom] [date] NULL,
	[AuditTo] [date] NULL,
	[ClientCode] [varchar](50) NULL,
	[EngagementCode] [varchar](50) NULL,
	[CreatedBy] [varchar](250) NULL,
	[CreatedDate] [date] NULL,
	[ModifiedBy] [varchar](255) NULL,
	[ModifiedDate] [datetime] NULL,
	[ExeVersionNo] [varchar](255) NULL,
	[ModuleName] [varchar](255) NULL,
	[EnteredOnMachineID] [varchar](255) NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[VPARAMETER2]    Script Date: 7/29/2020 7:11:09 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[VPARAMETER2](
	[Database] [nvarchar](255) NULL,
	[NUM] [nvarchar](255) NULL,
	[NAME] [nvarchar](255) NULL,
	[TYPE] [nvarchar](255) NULL,
	[VALUE] [nvarchar](255) NULL,
	[DISPLAY_VALUE] [nvarchar](255) NULL,
	[ISDEFA] [nvarchar](255) NULL,
	[ISSES] [nvarchar](255) NULL,
	[ISSYS_MOD] [nvarchar](255) NULL,
	[ISINS] [nvarchar](255) NULL,
	[ISMODIFIED] [nvarchar](255) NULL,
	[ISADJ] [nvarchar](255) NULL,
	[ISDEP] [nvarchar](255) NULL,
	[ISBAS] [nvarchar](255) NULL,
	[DESCRIPTION] [nvarchar](255) NULL,
	[ORDINAL] [nvarchar](255) NULL,
	[UPDATE_COMMENT] [nvarchar](255) NULL,
	[SessionID] [varchar](50) NULL,
	[ID] [varchar](50) NULL,
	[ClientID] [varchar](50) NULL
) ON [PRIMARY]
GO
ALTER TABLE [dbo].[Oracle_py_Output_attri_A] ADD  CONSTRAINT [DF_Oracle_py_Output_attri_A_SessionID]  DEFAULT ('1') FOR [SessionID]
GO
ALTER TABLE [dbo].[Oracle_py_Output_attri_B] ADD  CONSTRAINT [DF_Oracle_py_Output_attri_b_SessionID]  DEFAULT ('1') FOR [SessionID]
GO
/****** Object:  StoredProcedure [dbo].[DeleteDataFromTable]    Script Date: 7/29/2020 7:11:09 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO



-- =============================================
-- Author:	<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[DeleteDataFromTable] 
-- Add the parameters for the stored procedure here

@TableName varchar(200),@Filter VARCHAR(max)
AS
BEGIN

  SET NOCOUNT ON;
  DECLARE @query NVARCHAR(MAX);
  
  if (len(@Filter)>0)
  BEGIN
     set @query = 'delete top (100000) from ' + @TableName + ' where '+@Filter+';'
 end
 else
 BEGIN
  set @query = 'truncate table ' + @TableName 
 end

 while (@@ROWCOUNT >0)
 BEGIN
 EXECUTE( @query);
 end

END













GO
/****** Object:  StoredProcedure [dbo].[sprocDBIndexREBUILD]    Script Date: 7/29/2020 7:11:09 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO




CREATE PROC [dbo].[sprocDBIndexREBUILD] @FILLFACTOR INT = 85
AS
BEGIN
DECLARE @DatabaseName SYSNAME   = DB_NAME(),  @TableName VARCHAR(256) 
DECLARE @DynamicSQL NVARCHAR(max) =
'DECLARE curAllTablesInDB CURSOR FOR SELECT TABLE_SCHEMA +
''.'' + TABLE_NAME AS TABLENAME  
 FROM ' + @DatabaseName + '.INFORMATION_SCHEMA.TABLES WHERE
TABLE_TYPE = ''BASE TABLE'''  
         declare @var varchar(20)
         set @var='dbo.LedgerDetail'
BEGIN 
  EXEC sp_executeSQL @DynamicSQL  -- create tables cursor
  OPEN curAllTablesInDB  
  FETCH NEXT FROM curAllTablesInDB INTO @TableName  
  WHILE (@@FETCH_STATUS = 0) 
  BEGIN  
       SET @DynamicSQL = 'ALTER INDEX ALL ON ' + @TableName +
         ' REBUILD WITH ( FILLFACTOR = ' + CONVERT(VARCHAR,@FILLFACTOR) + ')' 
       PRINT @DynamicSQL;

         if( @TableName = @var)  
         Begin
                  print @var;
                  end
            else
            begin
                  EXEC sp_executeSQL @DynamicSQL 
          END 
       FETCH NEXT FROM curAllTablesInDB INTO @TableName  
   END   -- cursor WHILE
   CLOSE curAllTablesInDB  
   DEALLOCATE curAllTablesInDB 
END
END -- sproc














GO
/****** Object:  StoredProcedure [dbo].[UpdateIDForSSISInTable]    Script Date: 7/29/2020 7:11:09 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[UpdateIDForSSISInTable] 
-- Add the parameters for the stored procedure here
@TableName varchar(200),@SessionID varchar(50),@ClientCode varchar(60), @GetCount bigint output
AS
BEGIN
declare @CurrentDate varchar(50)
select @CurrentDate=CONVERT(varchar,getdate(),121)

  SET NOCOUNT ON;
  DECLARE @query NVARCHAR(MAX);
  declare @iRowCount bigint;
  DECLARE @intFlag INT
SET @intFlag = 1
 
WHILE (@intFlag <=5) 
BEGIN
begin transaction
 print '1'
SET @intFlag = @intFlag + 1
 set @query = 'update top (100000) ' + @TableName + ' set ID = NewID(),CreatedDate='''+@CurrentDate+''',ClientCode='''+@ClientCode+''',SessionID='''+@SessionID+''' where ID is null;'
  EXECUTE( @query);
select @iRowCount=@@rowcount;
 print '2'
 print (@query);
 
DECLARE @rowcount TABLE (Value bigint);
INSERT INTO @rowcount(Value)values(@iRowCount);
print '3'
SELECT @GetCount = Value FROM @rowcount;
commit
waitfor delay '00:00:00.001'
print '4'
END

END




GO
/****** Object:  StoredProcedure [dbo].[UpdateIDInTable]    Script Date: 7/29/2020 7:11:09 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO


-- =============================================
-- Author:	<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[UpdateIDInTable] 
-- Add the parameters for the stored procedure here

@TableName varchar(200), @GetCount bigint output
AS
BEGIN

  SET NOCOUNT ON;
  DECLARE @query NVARCHAR(MAX);
 set @query = 'update top (100000) ' + @TableName + ' set ID = NewID() where ID is null;'
 EXECUTE( @query);
 
DECLARE @rowcount TABLE (Value bigint);
INSERT INTO @rowcount
EXEC('select count(*) from  ' + @TableName + ' where ID is null;');
SELECT @GetCount = Value FROM @rowcount;

END













GO
/****** Object:  StoredProcedure [dbo].[UpdateZeroDayDateWithNullValue]    Script Date: 7/29/2020 7:11:09 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
create PROCEDURE [dbo].[UpdateZeroDayDateWithNullValue]
	-- Add the parameters for the stored procedure here
	@TableName varchar(200), @result bigint output
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

  declare @ColName varchar(50)
  declare @DataType varchar(50)
DECLARE @query NVARCHAR(MAX)
 declare @iRowCount bigint;

DECLARE upd_cursor CURSOR FOR 
select column_name,data_type from information_schema.columns where table_name=''+@TableName+'' and data_type like 'date%'
and column_name not in('AuditFrom','AuditTo','CreatedDate','ModifiedDate')

--print '1';

OPEN upd_cursor
FETCH NEXT FROM upd_cursor 
INTO @ColName,@DataType
--print '2';
--print @DataType;
--print '3';
WHILE @@FETCH_STATUS = 0
BEGIN
if @DataType='date'
BEGIN
set @query='IF EXISTS (SELECT 1 FROM ' + @TableName + '  WHERE ' +@ColName+ '=''1899-12-30'')
BEGIN
 update top (10000) '+@TableName+' set ' +@ColName+' = null  where '+@ColName+'=''1899-12-30''
END'
print (@query)
exec(@query)
select @iRowCount=@@rowcount;
-- set @query = 'Update ' + @TableName + '  SET ' +@ColName+ ' = null where '+ @ColName+ ' is not Null and ' +@ColName+ '=''1899-12-30''';
 --print '3';
 end
 else
 BEGIN
 set @query='IF EXISTS (SELECT 1 FROM ' + @TableName + '  WHERE ' +@ColName+ '=''1753-01-01 00:00:00.000'')
BEGIN
 update top (10000) '+@TableName+' set ' +@ColName+' = null  where '+@ColName+'=''1753-01-01 00:00:00.000''
END'
print (@query)
exec(@query)
 select @iRowCount=@@rowcount;
 --set @query = 'Update ' + @TableName + '  SET ' +@ColName+ ' = null where '+ @ColName+ ' is not Null and ' +@ColName+ '=''1753-01-01 00:00:00.000''';
 --print '4';
end 
--print (@Query);
 --EXECUTE( @query);
FETCH NEXT FROM upd_cursor 
INTO @ColName,@DataType
END
CLOSE upd_cursor
DEALLOCATE upd_cursor


 DECLARE @rowcount TABLE (Value bigint);
INSERT INTO @rowcount(Value)values(@iRowCount);
SELECT @result = Value FROM @rowcount;

	
END





GO
