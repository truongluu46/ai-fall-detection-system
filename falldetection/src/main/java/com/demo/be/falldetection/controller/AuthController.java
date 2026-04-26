package com.demo.be.falldetection.controller;

import com.demo.be.falldetection.dto.request.LoginRequest;
import com.demo.be.falldetection.entity.User;
import com.demo.be.falldetection.repositoty.UserRepository;
import lombok.AccessLevel;
import lombok.RequiredArgsConstructor;
import lombok.experimental.FieldDefaults;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/auth")
@RequiredArgsConstructor
@FieldDefaults(level = AccessLevel.PRIVATE, makeFinal = true)
public class AuthController {
    UserRepository userRepository;

    @PostMapping("/login")
    public String Login(@RequestBody LoginRequest request) {
        User user = userRepository.findByUsername(request.getUsername());

        if(user != null && user.getPassword().equals(request.getPassword())){
            return "LOGIN SUCCCESS";
        }
        return "FAIL";
    }
}
