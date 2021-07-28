
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
<th>ID</th>
<th>Page_number</th>
<th>Category</th>
<th>Working_English_title</th>
<th>Chinese_title</th>
</tr>
<xsl:for-each select="PA/corpus_text">
<tr>
<td><xsl:value-of select="ID"/></td>
<td><xsl:value-of select="Page_number"/></td>
<td><xsl:value-of select="Category"/></td>
<td><xsl:value-of select="Working_English_title"/></td>
<td><xsl:value-of select="Chinese_title"/></td>

</tr>
</xsl:for-each>
</table>
</body>
</html>
</xsl:template>
</xsl:stylesheet>
