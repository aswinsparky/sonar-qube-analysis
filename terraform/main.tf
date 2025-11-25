provider "aws" {
  region = "us-east-1"
}

# --- SECURITY GROUP (with secure SSH) ---
resource "aws_security_group" "sonarqube_sg" {
  name        = "sonarqube-sg"
  description = "Allow HTTP, HTTPS, and SonarQube UI access"
  tags = {
    Name        = "SonarQube-SG"
    Environment = "dev"
  }
}

resource "aws_security_group_rule" "ssh_in" {
  type              = "ingress"
  from_port         = 22
  to_port           = 22
  protocol          = "tcp"
  cidr_blocks       = ["YOUR_IP/32"] # REPLACE with your static IP!
  security_group_id = aws_security_group.sonarqube_sg.id
}

resource "aws_security_group_rule" "http_in" {
  type              = "ingress"
  from_port         = 80
  to_port           = 80
  protocol          = "tcp"
  cidr_blocks       = ["0.0.0.0/0"]
  security_group_id = aws_security_group.sonarqube_sg.id
}

resource "aws_security_group_rule" "https_in" {
  type              = "ingress"
  from_port         = 443
  to_port           = 443
  protocol          = "tcp"
  cidr_blocks       = ["0.0.0.0/0"]
  security_group_id = aws_security_group.sonarqube_sg.id
}

resource "aws_security_group_rule" "sonarqube_in" {
  type              = "ingress"
  from_port         = 9000
  to_port           = 9000
  protocol          = "tcp"
  cidr_blocks       = ["0.0.0.0/0"]
  security_group_id = aws_security_group.sonarqube_sg.id
}

resource "aws_security_group_rule" "egress_all" {
  type              = "egress"
  from_port         = 0
  to_port           = 0
  protocol          = "-1"
  cidr_blocks       = ["0.0.0.0/0"]
  security_group_id = aws_security_group.sonarqube_sg.id
}

# --- EC2 INSTANCE ---
resource "aws_instance" "sonarqube" {
  ami                    = "ami-0ecb62995f68bb549" # Update if needed
  instance_type          = "t2.medium"
  key_name               = "sonarqube-key"
  vpc_security_group_ids = [aws_security_group.sonarqube_sg.id]
  user_data              = file("${path.module}/sonarqube-install.sh")
  tags = {
    Name        = "SonarQube-Server"
    Environment = "dev"
    Owner       = "your-team"
  }
  root_block_device {
    volume_size = 40
    encrypted   = true
  }
  # Uncomment for AWS API access from EC2
  # iam_instance_profile = aws_iam_instance_profile.sonarqube_profile.name
}

# --- S3 BUCKET with ENCRYPTION and VERSIONING ---
resource "aws_s3_bucket" "sonarqube_reports" {
  bucket = "sonarqube-reports-your-unique-id" # Change to globally unique name
  tags = {
    Name        = "SonarQube-Reports"
    Environment = "dev"
  }
}

resource "aws_s3_bucket_versioning" "sonarqube_reports_versioning" {
  bucket = aws_s3_bucket.sonarqube_reports.id
  versioning_configuration {
    status = "Enabled"
  }
}

resource "aws_s3_bucket_server_side_encryption_configuration" "sonarqube_reports_encryption" {
  bucket = aws_s3_bucket.sonarqube_reports.id
  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}

# --- ROUTE 53 DNS (Zone and A record) ---
resource "aws_route53_zone" "main" {
  name = "sonarqube-example.com" # Replace with your domain
}

resource "aws_route53_record" "sonarqube" {
  zone_id = aws_route53_zone.main.zone_id
  name    = "sonar.sonarqube-example.com" # Replace as needed
  type    = "A"
  ttl     = 300
  records = [aws_instance.sonarqube.public_ip]
}

# --- USEFUL OUTPUTS ---
output "instance_ip" {
  value = aws_instance.sonarqube.public_ip
}
output "sonarqube_ui_url" {
  value = "http://${aws_instance.sonarqube.public_ip}:9000"
}
output "bucket_name" {
  value = aws_s3_bucket.sonarqube_reports.bucket
}
