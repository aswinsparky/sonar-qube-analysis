provider "aws" {
  region = "us-east-1"
}

# --- SECURITY GROUP (All bad practices!) ---
resource "aws_security_group" "sonarqube_sg" {
  name        = "sonarqube-sg"
  description = "Allow ALL Traffic"
}

# Allow SSH from anywhere (critical)
resource "aws_security_group_rule" "ssh_in" {
  type              = "ingress"
  from_port         = 22
  to_port           = 22
  protocol          = "tcp"
  cidr_blocks       = ["0.0.0.0/0"] # BAD: open to the world
  security_group_id = aws_security_group.sonarqube_sg.id
}

# Allow all protocols/all ports from anywhere (critical)
resource "aws_security_group_rule" "ssh_unrestricted" {
  type              = "ingress"
  from_port         = 0
  to_port           = 65535
  protocol          = "tcp"
  cidr_blocks       = ["0.0.0.0/0"]
  security_group_id = aws_security_group.sonarqube_sg.id
}

# No tags (minor)
# No description (minor)

# Resource using latest AMI instead of a pinned version (major)
resource "aws_instance" "sonarqube" {
  ami                    = "ami-latest" # BAD: Latest, not controlled, not versioned
  instance_type          = "t2.micro"
  key_name               = "hardcoded-key"        # BAD: secrets in code
  vpc_security_group_ids = [aws_security_group.sonarqube_sg.id]
  user_data              = file("${path.module}/sonarqube-install.sh")
  # No root_block_device encryption (critical)
  tags = {
    Name = "UnsecureSonarQube"
  }
}

# S3 bucket without encryption or versioning (major/critical)
resource "aws_s3_bucket" "vuln_bucket" {
  bucket = "sonarqube-insecure-bucket-demo"
  acl    = "public-read" # BAD: public bucket!
}

# S3 bucket policy allows full public access (critical)
resource "aws_s3_bucket_policy" "allow_all" {
  bucket = aws_s3_bucket.vuln_bucket.id
  policy = <<POLICY
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
    "Principal": "*",
    "Action": "s3:*",
    "Resource": [
      "${aws_s3_bucket.vuln_bucket.arn}",
      "${aws_s3_bucket.vuln_bucket.arn}/*"
    ]
  }]
}
POLICY
}

# Route 53 record: No vulnerability, kept for completeness.
resource "aws_route53_zone" "main" {
  name = "sonarqube-insecure.com"
}

resource "aws_route53_record" "sonarqube" {
  zone_id = aws_route53_zone.main.zone_id
  name    = "sonar.sonarqube-insecure.com"
  type    = "A"
  ttl     = 300
  records = [aws_instance.sonarqube.public_ip]
}

output "instance_ip" {
  value = aws_instance.sonarqube.public_ip
}
output "sonarqube_ui_url" {
  value = "http://${aws_instance.sonarqube.public_ip}:9000"
}
output "bucket_name" {
  value = aws_s3_bucket.vuln_bucket.bucket
}
