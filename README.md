# cst438project02

## Table of contents
* [General info](#general-info)
* [Structure](#structure)
* [Setup](#setup)

## General info
Using the agile process to research, develop, deploy, and present a full stack of wishlist application. The goal of this team project is to design and implement a web wishlist application by using modern web frameworks. Required development are Representational state transfer (REST), Application Programming Interface (API), a constant integration, constant development pipline, and a persistence (Database) layer. 

## Structure
Back-end/Front-end:
* Django [link] (https://www.djangoproject.com/)

Research Database Tech:
* SQLite

Required API endpoints and parameters
* Create new user account: POST: [url]/newuser?username={username}&password={password}
* Log in to account: POST: [url]/login?username={username}&password={password}
* Log out of account POST/GET [url]/logout?username={username}
* Delete account: DELETE [url]/logout?username={username}
* List all items: GET [URL]/items
* Show a specific list: GET [URL]/items?list={list name || list ID} OR GET [URL]/items?user={user id}&list={list name || list ID}
* Show a specific item: GET [URL]/items?itemID;
* Add new items: POST [URL]/items?item_name={item name}&url={url}
* Remove items: DELETE [URL]/items?item_name={item id}
* Update items: PATCH [URL]/items?item_name={item id}


"Creating something like Gifthero.com"

### Project Team:
Keyoni: https://github.com/keyoni
Makayla: https://github.com/makayla-k
Oscar: https://github.com/csramirez
Sophia: https://github.com/jenlopez1411
