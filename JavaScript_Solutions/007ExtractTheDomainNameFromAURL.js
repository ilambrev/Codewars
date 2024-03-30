function domainName(url) {

    let domainName = url;

    if (domainName.includes('www')) {
        domainName = domainName.substring(indexOfElement(domainName, '.') + 1);
    } else if (domainName.includes('//')) {
        domainName = domainName.substring(indexOfElement(domainName, '//') + 2);
    }

    domainName = domainName.substring(0, indexOfElement(domainName, '.'));

    function indexOfElement(domainName, element) {
        return domainName.indexOf(element);
    }

    return domainName;

}

// domainName("http://github.com/carbonfive/raygun");
// domainName("http://www.zombie-bites.com");
// domainName("https://www.cnet.com");
// domainName("84pvs.name/warez/");
// domainName("zdhst99g9i2o-5i.it/archive/");