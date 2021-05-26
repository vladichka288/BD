const puppeteer = require("puppeteer");
fs = require("fs");
var parser = require("xml2json");
var convert = require("xml-js");
var xpath = require("xpath"),
  dom = require("xmldom").DOMParser;

function getCountTextFragment(array) {
  let count = 0;
  for (let i = 0; i < array.length; i++) {
    if ((array[i]._attributes.type = "image")) {
      count++;
    }
  }
  return count;
}
(async () => {
  try {
    //TASK1
    //TASK1
    //TASK1
    /*
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    await page.goto("https://kpi.ua/");
    let bodyHTML = await page.evaluate(() => document.body.innerHTML);
    var doc = new dom().parseFromString(bodyHTML);
    let allPagesNodes = xpath.select("//a//@href", doc);
    let counter = 0;
    let allPagesUrls = [];

    for (let i = 0; i < allPagesNodes.length; i++) {
      if (counter != 13) {
        if (allPagesNodes[i].value.startsWith("http") && counter < 20) {
          allPagesUrls.push(allPagesNodes[i].value);
          counter++;
        }
      } else {
        counter++;
      }
    }

    const functionWithPromise = (item) => {
      return Promise.resolve(item);
    };
    const anAsyncFunction = async (url) => {
      const page = await browser.newPage();
      await page.goto(url);
      let bodyHTML = await page.evaluate(() => document.body.innerHTML);
      let bodyText = await page.evaluate(
        () => `\n${document.body.innerText}\n`
      );
      let bodyTextArray = bodyText.split("\n");
      let filtredTextArray = bodyTextArray.filter(
        (string) => string.trim() != ""
      );
      let doc = new dom().parseFromString(bodyHTML);
      let imgNodes = xpath.select("//img/@src", doc);

      let FragmentsObjects = [];
      for (let i = 0; i < imgNodes.length; i++) {
        FragmentsObjects.push({
          _attributes: { type: "image" },
          _text: imgNodes[i].value,
        });
      }

      for (let i = 0; i < filtredTextArray.length; i++) {
        FragmentsObjects.push({
          _attributes: { type: "text" },
          _text: filtredTextArray[i],
        });
      }
      return functionWithPromise({
        fragment: FragmentsObjects,
        _attributes: { url: url },
      });
    };
    allPagesUrls.unshift("https://kpi.ua/");
    const getData = async () => {
      return Promise.all(allPagesUrls.map((url) => anAsyncFunction(url)));
    };
    arrayOfObjectsFromPages = await getData();
    let resultObjectFromArray = [];
    for (let i = 0; i < arrayOfObjectsFromPages.length; i++) {
      resultObjectFromArray.push({ ...arrayOfObjectsFromPages[i] });
    }
    const resultObject = {
      data: { page: resultObjectFromArray },
    };
    var options = { compact: true, ignoreComment: true, spaces: 4 };
    let result = convert.js2xml(resultObject, options);

    await browser.close();
    fs.writeFile("./result.xml", result, function (err) {
      if (err) {
        return console.log(err);
      }

      console.log("The file was saved!");
    });
*/
    //TASK1
    //TASK1
    //TASK1

    //TASK2
    //TASK2
    //TASK2

    var options = { compact: true, ignoreComment: true, spaces: 4 };
    let xml = fs.readFileSync("./result.xml", "utf8");
    let jsObjectFromXML = convert.xml2js(xml, options);
    let pages = jsObjectFromXML.data.page;
    let maxIndex = 0;

    for (let i = 0; i < pages.length - 1; i++) {
      if (
        getCountTextFragment(pages[maxIndex].fragment) <
        getCountTextFragment(pages[i].fragment)
      ) {
        maxIndex = i;
      }
    }
    console.log(maxIndex+1);
  
    //TASK2
    //TASK2
    //TASK2

    //TASK3
    //TASK3
    //TASK3

    
    const browser = await puppeteer.launch();
    const page = await browser.newPage();

    await page.goto("https://rozetka.com.ua/ua/");

    let bodyHTML = await page.evaluate(() => document.body.innerHTML);
    var doc = new dom().parseFromString(bodyHTML);
    let allProductsSrcNodes = xpath.select("//a/img[@rzimgui]/@src", doc);
    let allProductsDescriptionNodes = xpath.select(
      "//app-tile/div/div/a/@title",
      doc
    );
    let allProductsPriceNodes = xpath.select(
      `//span[@class="tile__price-value"]/text()`,
      doc
    );
 
    let arrayOfProducts = [];
    for (let i = 0; i < 16; i++) {
      if (allProductsPriceNodes[i]) {
        let productObject = {
          price: allProductsPriceNodes[i].nodeValue.trim(),
          image: allProductsSrcNodes[i].value,
          description: allProductsDescriptionNodes[i].value,
        };
        arrayOfProducts.push(productObject);
      }
    }
    let resultObject = { data: { product: arrayOfProducts } };
    var options = { compact: true, ignoreComment: true, spaces: 4 };
    let result = convert.js2xml(resultObject, options);

    await browser.close();
    console.log("chiha");
    fs.writeFile("./products.xml", result, function (err) {
      if (err) {
        return console.log(err);
      }

      console.log("The file was saved!");
    });
    
  } catch (err) {
    console.log(err);
  }
})();
