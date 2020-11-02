USE AMTRAK_DEVRAW 
GO
/*
Those members which are null in the MRE tables, they are assigned as 'memberid' whereas in EI side, any null members are assigned as '~N'. So in order to avoid any null insert into factevents, this patch is executed. 
*/

IF EXISTS (SELECT 1 FROM EA_EA_OFFICEVISITS WHERE MEMID ='memberid')
BEGIN
	UPDATE EA_EA_OFFICEVISITS
	SET  MEMID='~N'
	WHERE MEMID ='memberid'
END

GO

IF EXISTS (SELECT 1 FROM EA_EA_OFFICEVISITS WHERE MEMID ='memberid')
BEGIN
	UPDATE EA_EA_OFFICEVISITS
	SET  MEMID='~N'
	WHERE MEMID ='memberid'
END

IF EXISTS (SELECT 1 FROM EA_EA_ADMISSIONS WHERE MEMID ='memberid')
BEGIN
	UPDATE EA_EA_ADMISSIONS
	SET  MEMID='~N'
	WHERE MEMID ='memberid'
END
GO
IF EXISTS (SELECT 1 FROM EA_EA_ERVISITS WHERE MEMID ='memberid')
BEGIN
	UPDATE EA_EA_ERVISITS
	SET  MEMID='~N'
	WHERE MEMID ='memberid'
END
GO



