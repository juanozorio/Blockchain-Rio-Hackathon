'use client'
import CarouselBanner from '../components/CarouselBanner/CarouselBanner';
import Menu from '../components/Menu';
import Card from '../components/Card';
import Taba from '@/components/Taba/Taba';
import SubMenu from '@/components/SubMenu/Index';
import Footer from '@/components/Footer';

export default function Home() {
  return (
    <>
      <SubMenu />
      <CarouselBanner />

      <Card description={'aloha caption'} title={'title aqui'} />
    </>
  );
}