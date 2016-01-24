/*
Navicat PGSQL Data Transfer

Source Server         : localhost
Source Server Version : 90500
Source Host           : localhost:5432
Source Database       : db
Source Schema         : public

Target Server Type    : PGSQL
Target Server Version : 90500
File Encoding         : 65001

Date: 2016-01-14 22:14:16
*/


-- ----------------------------
-- Table structure for mail
-- ----------------------------
DROP TABLE IF EXISTS "public"."mail";
CREATE TABLE "public"."mail" (
"id" int2 DEFAULT nextval('mail_id'::regclass) NOT NULL,
"theme" varchar COLLATE "default",
"to" varchar(255) COLLATE "default",
"from" varchar(255) COLLATE "default",
"message" text COLLATE "default"
)
WITH (OIDS=FALSE)

;

-- ----------------------------
-- Records of mail
-- ----------------------------
INSERT INTO "public"."mail" VALUES ('31', 'ewrwer', 'asf@dfgfdg.ru', 'qgfgwe@qwe.ru', '75474');
INSERT INTO "public"."mail" VALUES ('37', 'hello', 'asd@qwe.ru', 'test@qwe.ru', 'Test message!');

-- ----------------------------
-- Alter Sequences Owned By 
-- ----------------------------

-- ----------------------------
-- Primary Key structure for table mail
-- ----------------------------
ALTER TABLE "public"."mail" ADD PRIMARY KEY ("id");
