# Copyright (c) 2024, thinkspedia and contributors
# For license information, please see license.txt

import binascii
import frappe
import os
import base64
import requests
from frappe.model.document import Document
from frappe.utils.file_manager import save_file, get_file, get_file_name

class MemberPhoto(Document):
    # def before_save(self):
    #     if self.photo:
    #         # Menambahkan padding jika panjang base64 tidak valid
    #         missing_padding = len(self.photo) % 4
    #         if missing_padding:
    #             self.photo += '=' * (4 - missing_padding)

    #         # Mendekode base64 menjadi bytes
    #         try:
    #             file_content = base64.b64decode(self.photo)
    #         except binascii.Error as e:
    #             frappe.throw(f"Error decoding base64: {str(e)}")

    #         # Membuat nama file baru
    #         new_file_name = "{0}_adz.jpg".format(self.member_id)
            
    #         # Menyimpan file dengan nama baru dalam format biner
    #         file_url = save_file(new_file_name, content=file_content, 
    #                              dt=self.doctype, dn=self.name)

    #         # Update URL ke file yang baru diunggah
    #         self.photo = file_url
    
    
    # def before_save(self):
    #     if self.photo:
    #         # Ambil dokumen file berdasarkan file_url
    #         file_doc = frappe.get_doc('File', {'file_url': self.photo})
            
    #         # Ambil konten file dalam format biner
    #         file_content = file_doc.get_content()
            
    #         # Tentukan nama file baru
    #         new_file_name = "{0}_adz.jpg".format(self.member_id)
            
    #         # Simpan file baru dengan nama yang diubah
    #         file_url = save_file(new_file_name, content=file_content, 
    #                              dt=self.doctype, dn=self.name)
            
    #         # Perbarui field photo dengan file_url yang baru
    #         self.photo = file_url


    # def before_save(self):
    #     if self.photo:
    #         # file_name = get_file_name(self.photo)
    #         file_content = base64.b64decode(self.photo)
    #         new_file_name = "{0}_adz.jpg".format(self.member_id)
    #         file_url = save_file(new_file_name, content=file_content, 
    #                              dt=self.doctype, dn=self.name)
    #         self.photo = file_url

    # def after_save(self):
    #     # Cek apakah ada file attachment
    #     if self.photo:
    #         # Proses file attachment
    #         frappe.log("###### MASUK DATA POTO ! ######")
    #         self.handle_file_attachment()
    #     else:
    #         frappe.log_error("No file URL found for the MemberPhoto document.")

    # def handle_file_attachment(self):
    #     try:
    #         frappe.log("###### handle_file_attachment ######")
    #         # Tentukan direktori 'photos' di dalam site
    #         photos_dir = get_site_path('photos')

    #         # Buat folder 'photos' jika belum ada
    #         if not os.path.exists(photos_dir):
    #             os.makedirs(photos_dir)

    #         # Ambil member_id
    #         member_id = self.member_id
    #         frappe.log("###### MEMBER_ID ######", member_id)

    #         # Tentukan nama file dengan member_id
    #         file_name = f"{member_id}.jpg"  # Sesuaikan ekstensi file sesuai kebutuhan Anda

    #         # Tentukan path file
    #         file_path = os.path.join(photos_dir, file_name)

    #         # Dapatkan dokumen file
    #         file_doc = frappe.get_doc("File", self.photo)
    #         if not file_doc:
    #             frappe.log_error("File document not found.")
    #             return

    #         # Simpan file dari attachment ke lokasi yang diinginkan
    #         with open(file_path, 'wb') as f:
    #             f.write(file_doc.get_content())
            
    #         # Update kolom di DocType
    #         self.file_path = file_path
    #         self.file_name = file_name

    #         # Panggil fungsi untuk post API setelah data disimpan
    #         # self.post_image_as_base64()
    #         frappe.msgprint("File saved successfully to photos directory.")
    #     except Exception as e:
    #         frappe.log_error(f"Error in handle_file_attachment: {str(e)}")
    #         frappe.throw(f"Error in handle_file_attachment: {str(e)}")

    # def post_image_as_base64(self):
    #     try:
    #         # Baca file gambar
    #         with open(self.file_path, "rb") as image_file:
    #             # Encode gambar ke base64
    #             base64_image = base64.b64encode(image_file.read()).decode('utf-8')

    #         # Buat payload untuk API
    #         payload = {
    #             "member_id": self.member_id,
    #             "image": base64_image
    #         }

    #         # URL API tujuan
    #         api_url = "https://your-api-url.com/endpoint"  # Sesuaikan dengan URL API Anda

    #         # Header (jika ada token atau content-type yang dibutuhkan)
    #         headers = {
    #             "Content-Type": "application/json"
    #         }

    #         # Lakukan POST request
    #         response = requests.post(api_url, json=payload, headers=headers)

    #         # Cek respons API
    #         if response.status_code == 200:
    #             frappe.msgprint("Image successfully sent to API.")
    #         else:
    #             frappe.msgprint(f"Failed to send image to API. Status Code: {response.status_code}")
    #     except Exception as e:
    #         frappe.log_error(f"Error in post_image_as_base64: {str(e)}")
    #         frappe.throw(f"Error in post_image_as_base64: {str(e)}")