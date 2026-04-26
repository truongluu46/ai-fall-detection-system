package com.demo.be.falldetection.repositoty;

import com.demo.be.falldetection.entity.User;
import org.springframework.data.jpa.repository.JpaRepository;

public interface UserRepository extends JpaRepository<User, Long> {
    User findByUsername(String username);
}
