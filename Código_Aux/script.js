const puppeteer = require('puppeteer');

async function generatePDF(htmlContent, outputPath) {
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    
    // Configurando o conteúdo HTML da página
    await page.setContent(htmlContent);
    
    // Gerando o PDF
    await page.pdf({ path: outputPath, format: 'A4' });

    await browser.close();
    console.log(`PDF gerado em: ${outputPath}`);
}

// Exemplo de uso
const htmlContent = `
<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-0lax{text-align:left;vertical-align:top}
</style>
<table class="tg"><thead>
  <tr>
    <th class="tg-0lax">Nome do Campo</th>
    <th class="tg-0lax"> Descrição</th>
    <th class="tg-0lax"> Tipo de Dados</th>
    <th class="tg-0lax"> Restrições</th>
  </tr></thead>
<tbody>
  <tr>
    <td class="tg-0lax">CODIGO_UF</td>
    <td class="tg-0lax"> Código da UF</td>
    <td class="tg-0lax"> INTEGER</td>
    <td class="tg-0lax"> PRIMARY KEY</td>
  </tr>
  <tr>
    <td class="tg-0lax">SIGLA_UF</td>
    <td class="tg-0lax"> Sigla da UF</td>
    <td class="tg-0lax"> TEXT</td>
    <td class="tg-0lax"> </td>
  </tr>
  <tr>
    <td class="tg-0lax">NOME_UF</td>
    <td class="tg-0lax"> Nome da UF</td>
    <td class="tg-0lax"> TEXT</td>
    <td class="tg-0lax"> </td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
  </tr>
</tbody>
</table>
`;

const outputPath = '../Dicionários/Dict_MUNICIPIOS.pdf';
generatePDF(htmlContent, outputPath);
