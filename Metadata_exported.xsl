
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
<xsl:output method="html"/>
<xsl:template match="/">
<html>
<head>
</head>
<body>
	<h1>Uyghur-Chinese Corpus</h1>
<table border="1">
<tr bgcolor="#9acd32">
<th>Folder_Name</th>
<th>Genre</th>
<th>Period-Region</th>
<th>Author</th>
<th>English_Title-Description</th>
<th>File_Name</th>
<th>Turkish-Uyghur_Title-Description</th>
<th>Turkish-Uyghur_Source</th>
<th>T-U_Publication_Date</th>
<th>Chinese_Title-Description</th>
<th>Chinese_Source</th>
<th>Chinese_Publication_Date</th>
<th>Remark</th>
</tr>
<xsl:for-each select="Metadata/corpus_text">
<tr>
<td><xsl:value-of select="Folder_Name"/></td>
<td><xsl:value-of select="Genre"/></td>
<td><xsl:value-of select="Period-Region"/></td>
<td><xsl:value-of select="Author"/></td>
<td><xsl:value-of select="English_Title-Description"/></td>
<td><xsl:value-of select="File_Name"/></td>
<td><xsl:value-of select="Turkish-Uyghur_Title-Description"/></td>
<td><xsl:value-of select="Turkish-Uyghur_Source"/></td>
<td><xsl:value-of select="T-U_Publication_Date"/></td>
<td><xsl:value-of select="Chinese_Title-Description"/></td>
<td><xsl:value-of select="Chinese_Source"/></td>
<td><xsl:value-of select="Chinese_Publication_Date"/></td>
<td><xsl:value-of select="Remark"/></td>

</tr>
</xsl:for-each>
</table>
</body>
</html>
</xsl:template>
</xsl:stylesheet>
