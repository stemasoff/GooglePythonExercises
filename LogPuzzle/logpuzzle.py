import os
import re
import sys
import urllib.request


def read_urls(filename):
	patternToSearchLink = r'GET (.*-\w*.jpg).(\w*)'
	urlServer = re.search(r'_(.*)', filename).group(1)

	with open(filename, 'r') as inputLog:
		logData = inputLog.read()

	urls = re.findall(patternToSearchLink, logData)

	for i in range(len(urls)):
		urls[i] = urls[i][1] + '://' + urlServer + urls[i][0]

	urls.sort()
	print('Duplicate URLs:')
	for url in urls:
		if urls.count(url) > 1:
			print(url)
			startSlice = urls.index(url) + 1
			endSlice = startSlice + urls.count(url)
			del urls[startSlice: endSlice]

	if re.search(r'-\w*-\w*.jpg', urls[0]):
		dictForSorting = {}
		for url in urls:
			wordToSort = re.search(r'\w*.jpg', url).group()
			dictForSorting[wordToSort] = url

		sortKeys = list(dictForSorting.keys())
		sortKeys.sort()

		urls.clear()
		for key in sortKeys:
			urls.append(dictForSorting[key])

	return urls


def download_images(imageUrls, destDir):
	if os.path.exists(destDir) is not True:
		os.mkdir(destDir)

	index = 0
	sources = []
	for url in imageUrls:
		nameImage = f'img{index}.jpg'
		print(f'Retrieving {url}')
		fullName = destDir + nameImage
		urllib.request.urlretrieve(url, fullName)
		sources.append(fullName)
		index += 1

	with open('index.html', 'w') as outputFile:
		imageTags = ''
		for source in sources:
			tag = f'<img src="{source}">'
			imageTags = imageTags + tag

		template = '<verbatim>\n' \
				   '<html>\n' \
				   '<body>\n' \
				   + imageTags \
				   + '\n</body>\n' \
					 '</html>'
		outputFile.write(template)


def main():
	args = sys.argv[1:]

	if not args:
		print('usage: [--todir dir] logfile ')
		sys.exit(1)

	todir = ''
	if args[0] == '--todir':
		todir = args[1]
		del args[0:2]

	imageUrls = read_urls(args[0])
	if todir:
		download_images(imageUrls, todir)


if __name__ == '__main__':
	main()
