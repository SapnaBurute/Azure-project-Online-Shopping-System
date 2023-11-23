# Azure-project-Online-Shopping-System
Future Ready Talent - Project Documentation

<h1>Project Title – A2Z online shopping</h1>


<h2>Project Statement</h2>

<h2>Project Aim</h2> <br>
The project aim for online shopping system is to develop a web-based application that can provide an online shopping feature to users. The project aims to create a virtual shop environment for users, where they can browse, search, select, and purchase products from different categories and vendors. The project also aims to provide a secure and reliable payment system, a user-friendly interface, and a database management system for storing and retrieving product and customer information. The project can benefit both customers and sellers, as it can offer convenience, variety, competitive prices, and global access. <br>
The aim of this project is to develop a web-based application that can provide an online shopping feature to users. The application will allow users to browse, search, select, and purchase products from different categories and vendors, using a secure and reliable payment system. The application will also have a user-friendly interface and a database management system for storing and retrieving product and customer information. The project will benefit both customers and sellers, as it will offer convenience, variety, competitive prices, and global access. The project will also contribute to the advancement of e-commerce and web development technologies.<br>


<h2>Description </h2>

 	Online Shopping Application is a web-based project that allows users to shop online from various categories and vendors. Users can browse, search, select, and purchase products using a secure and reliable payment system. The project also provides a user-friendly interface and a database management system for storing and retrieving product and customer information. The project aims to create a virtual shop environment for users, where they can enjoy the convenience, variety, competitive prices, and global access of online shopping. The project also uses the latest web development technologies and follows the best practices of e-commerce. <br>

<h2>Key Features:</h2>

1.	Home Page:

     Users can easily upload their images through a user-friendly interface. The application supports a variety of image formats, such as JPEG, PNG, and GIF.

2.	Product Feature:
This feature allows the online shopping system to display the products that are available for sale in different categories, such as men, women, kids, etc. The products have detailed descriptions, images, prices, ratings, reviews, and availability information.

3.	Admin Feature:

This feature allows the online shopping system to be managed by the administrator, who can add, edit, delete, and update the products, categories, vendors, orders, customers, and other information. The admin feature also allows the administrator to monitor the sales, inventory, revenue, and performance of the online shopping system.

4.	Cart Feature:

This feature allows the online shopping system to store the products that the users have selected for purchase in their shopping cart. The cart feature also allows the users to modify, remove, or save the products in their cart, as well as view the subtotal, tax, shipping, and total amount of their order.

5.	Log In & Sign Up:

Log in and sign up are key features of any online system that requires users to create and access their accounts. These features allow users to register, log in, and manage their profiles, preferences, and settings.

6.	Scalability:

Leveraging Azure App Service, the application can seamlessly handle increased traffic and demand. It can be auto-scaled to accommodate varying numbers of users and concurrent uploads.

7.	Data Storage:

Uploaded images and their associated information are securely stored in Azure Blob Storage or a similar data repository. This ensures reliable and durable storage for the uploaded content.

The application is designed to be responsive, ensuring it works seamlessly on various devices, including desktops, tablets, and smartphones.
Analytics and Monitoring:

Utilize Azure Application Insights to monitor the application's performance, track usage, and identify potential issues for quick resolution.
Deployment:
The Image Upload and Display Application can be deployed on Azure App Service, which offers a fully managed platform for building, deploying, and scaling web apps. The deployment process includes configuring the web app, setting up the database or data storage, and enabling any necessary security measures and scaling options.

This project is ideal for individuals or businesses looking to create a user-friendly and scalable image-sharing platform. Whether it's for personal photo collections or a community-driven image repository, the Azure-based Image Upload and Display Application offers a robust and reliable solution.
<br>



<h1>Azure Services Used –</h1>
<h2>Virtual Machine </h2>
<h2>Load Balancer</h2>
<h2>Azure Storage account</h2>

<h2>Other Services Used</h2> – 
Bash Scripts
Network security group<br>

<h2>Environment Used-</h2>
VM – Linux (ubuntu 20.04)
System – Windows 11<br>


<h2>Project Walkthrough</h2>


o	Create an Azure free account, sign into my Azure Portal<br>
o	Click on virtual machine tab, create virtual machine <br>

![virtual machine](https://github.com/SapnaBurute/Azure-project-Online-Shopping-System/assets/134684026/3fa8393b-81d0-449f-8c8d-0adca4334550) <br> 

o Subscription- Free Trial
o Resource group- azure-trial
o Virtual machine name- online-shopping
o Region- Central India

 o Leave disks tab as default <br>
 

![create vm](https://github.com/SapnaBurute/Azure-project-Online-Shopping-System/assets/134684026/c02266a7-909a-48c1-9335-1c932560cbd2)<br>


<h2>Connect to virtual machines
There are several ways to access your Azure virtual machines. The Azure portal supports options for connecting your Windows and Linux machines, and making connections by using Azure Bastion. The following diagram shows how you can connect Azure virtual machines with the SSH and RDP protocols, Cloud Shell, and Azure Bastion.
 
<h2>Architecture diagram</h2>

![vm network](https://github.com/SapnaBurute/Azure-project-Online-Shopping-System/assets/134684026/65047736-854b-4961-9311-d0fddb3bda26)
<br>






<h2>NOW CREATE A STORAGE ACCOUNT</h2>

o Subscription- Free Trial
o Resource group- azure-trial
o Storage account Name- photosto11
o Region- central(india) <br>

![storage account](https://github.com/SapnaBurute/Azure-project-Online-Shopping-System/assets/134684026/181488eb-fe26-4ecb-9d56-c9c375e10b61)


 




I have created Storage accounts  to store and manage photo in cloud environments, typically in the context of cloud computing platforms like Microsoft Azure,. They serve several important purposes:

Data Storage: Storage accounts provide a secure and scalable place to store various types of data, such as files, blobs, tables, queues, and virtual machine disks.

Scalability: They can scale to accommodate growing amounts of data, making them suitable for a wide range of applications, from small projects to large enterprises.

Data Redundancy: Storage accounts often offer features like data replication and redundancy to ensure data durability and availability. This means your data is stored in multiple locations, reducing the risk of data loss.

Accessibility: They allow you to access and manage your data over the internet or within a cloud network, making it accessible from anywhere.

Integration: Storage accounts can be integrated with various cloud services and applications, enabling you to build and deploy solutions that require data storage, retrieval, and processing.

Security: They offer security features, such as access control, encryption, and authentication, to protect your data from unauthorized access and breaches.

Cost Management: Cloud providers typically offer different storage tiers with varying costs, so you can choose the most cost-effective option for your specific use case.

In summary, storage accounts are a fundamental component in cloud computing, offering reliable and scalable data storage solutions for a wide range of applications and services.

<h2>CONNECT STORAGE ACCOUNT TO WEBSITE</h2>

•	First go to access key of storage account
•	Copy the connection string of storage account and paste into code <br>


![Acess keys](https://github.com/SapnaBurute/Azure-project-Online-Shopping-System/assets/134684026/833724b5-f816-4401-b892-7d54b15c53f7)

 


•	I have created storage account to store photos which any user will upload in my website


•	Storage accounts are used for a variety of purposes in the context of cloud computing, particularly in platforms like Microsoft Azure. Here are some common reasons why storage accounts are used:

•	Data Storage: Storage accounts are primarily used to store data, including files, documents, images, videos, and more. They provide scalable and reliable storage options for both structured and unstructured data.

•	Backup and Recovery: Storage accounts can be used to create backups of your data, ensuring data resilience and enabling recovery in case of data loss or disasters.



<h2>NOW CONNECT THE VM SSH USING AZURE CLI</h2>



![vm cli](https://github.com/SapnaBurute/Azure-project-Online-Shopping-System/assets/134684026/7f6ccd25-1538-4d0a-8e08-96514188d64b)
<br>

 


<h2>NOW IN TERMINAL WRITE THE COMMAND</h2>

1.	sudo apt update && sudo apt upgrade –y
2.	sudo apt install python3 python3-pip git -y
3.	sudo apt install django , pillow
4.	mkdir app
5.	cd app<br>

![connect vm 2](https://github.com/SapnaBurute/Azure-project-Online-Shopping-System/assets/134684026/eec8c7db-f493-4206-b1ce-25cf28457a26)

<br>

<h2>OPEN THE INBOUND PORT OF VM</h2>

![run vm](https://github.com/SapnaBurute/Azure-project-Online-Shopping-System/assets/134684026/93c05a60-3db6-4bbd-883b-80ce2a695284)

<br>
 
<h2>GIT CLONE</h2>

![connect vm 2](https://github.com/SapnaBurute/Azure-project-Online-Shopping-System/assets/134684026/eec8c7db-f493-4206-b1ce-25cf28457a26) <br>

<h2>Now the run the command python3 aap.py</h2>

 
![run vm](https://github.com/SapnaBurute/Azure-project-Online-Shopping-System/assets/134684026/93c05a60-3db6-4bbd-883b-80ce2a695284) <br>


<h2>OUTPUT</h2> 

![home page](https://github.com/SapnaBurute/Azure-project-Online-Shopping-System/assets/134684026/62255ec4-30ba-4596-b2b0-260b380cb8b9)
<br>

<h2>SIGN UP</h2>

 ![sign up page](https://github.com/SapnaBurute/Azure-project-Online-Shopping-System/assets/134684026/08e30e9b-2a38-4867-b257-f33c29bbea7a)
 <br>


<h2>LOGIN PAGE</h2>

![login page](https://github.com/SapnaBurute/Azure-project-Online-Shopping-System/assets/134684026/1c517844-98f0-4efa-a852-2a0dcc152d4b)
<br>
 

<h2>your cart Page</h2>

 
![your cart](https://github.com/SapnaBurute/Azure-project-Online-Shopping-System/assets/134684026/d2025c51-3ebd-4c4d-b4a9-546027dde3c1)
<br>

<h2>Conclusion</h2>


<h2>Project Conclusion-</h2>

In conclusion, the online shopping application is a web-based project that allows users to shop online from various categories and vendors. The project uses virtual machine, load balancer, and storage account to provide a scalable, reliable, and secure solution for the online shopping system.

Users can easily upload their images, enrich them with essential information, and navigate their collection with ease. The application's search and filter functionality enhance user experience, while responsive design ensures accessibility across different devices.

The project uses storage account to store and access the data and files related to the online shopping application. The storage account provides durability, security, and scalability for the data and files. The project also uses blob storage, table storage, and queue storage to store different types of data and files, such as product images, product information, customer information, and order information.

The project provides a user-friendly interface and a database management system for the online shopping application. The project also provides features such as search, navigation, cart, checkout, payment, user account, customer service, and feedback for the online shopping application. The project aims to create a virtual shop environment for users, where they can enjoy the convenience, variety, competitive prices, and global access of online shopping.<br>

<h2>Project link :</h2> http://4.240.64.124:8000/
<h2>Project Video Link:</h2>  https://drive.google.com/file/d/1j85_eHKVJTNrgp1Bsxf6onFcD8A-yIB4/view?usp=drive_link
